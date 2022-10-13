from time import time
from django.db import models
from django.utils import timezone

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField('Release Date', default=timezone.now)
    genre = models.CharField(max_length=255)