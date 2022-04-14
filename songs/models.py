from django.db import models

class Song (models.Model):
  name = models.CharField(max_length=200)
  # album = models.CharField(max_length=100)
  # artist = models.CharField(max_length=100)
  description = models.CharField(max_length=300)
  spotify_link = models.CharField(max_length=200)

  def __str__(self):
    return self.name



