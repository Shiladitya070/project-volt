from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

class Post (models.Model):
    title = models.CharField(max_length = 100 )
    content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.datetime.now())
    # print(date_posted)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs= {'pk': self.pk})

        
