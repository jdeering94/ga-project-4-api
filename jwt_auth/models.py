from django.db import models
from songs.models import Song
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  image = models.CharField(max_length=200)
  liked_songs = models.ManyToManyField(Song, related_name='liked_by', blank=True)

  def __str__(self):
    return f"{self.username}"