from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class ApiCall(models.Model):
    name = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('api-home', kwargs={'pk': self.pk})


class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
