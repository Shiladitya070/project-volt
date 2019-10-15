from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Just a new user . Add your bio')
    # image = models.ImageField(default='default.jpg', upload_to= 'profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
