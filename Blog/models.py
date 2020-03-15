from django.db import models

# Create your models here.

# Posts


class Blog(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=1000)
    mainContent = models.CharField(max_length=200000)
    user = models.CharField(max_length=100)
    date = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    blogtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# BlogConfiguration


class Blogconf(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=1000)
    description = models.CharField(max_length=150)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.user
# Comments
# Create your models here.


class Comment(models.Model):
    user = models.CharField(max_length=100)
    mainContent = models.CharField(max_length=10000)
    url = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.user
