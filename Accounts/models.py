from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
# User
class Profile(models.Model):
    user = models.CharField(max_length=100)
    picture = models.CharField(
        max_length=1000, default='https://wikicdn.web.app/media/cat.png')
    description = models.CharField(
        max_length=1000, default='there is nothing here')
    profilepicture = models.CharField(
        max_length=1000, default="https://wikicdn.web.app/media/cat.png")

    def __str__(self):
        return self.user
