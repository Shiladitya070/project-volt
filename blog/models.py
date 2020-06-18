from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
User = get_user_model()


class Post (models.Model):
    title = models.CharField(max_length=1000)
    content = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def count_posts_of(user):
        return Post.objects.filter(author=user).count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name="post", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="author")
    comment_content = models.CharField(max_length=200, verbose_name="comment")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
