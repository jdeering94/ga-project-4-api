from django.db import models

class Artist (models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Song (models.Model):
  name = models.CharField(max_length=200)
  # album = models.CharField(max_length=100)
  artist = models.ForeignKey(Artist, related_name='songs', max_length=50, on_delete=models.CASCADE)
  year = models.IntegerField()
  description = models.CharField(max_length=300)
  spotify_link = models.CharField(max_length=200)

  def __str__(self):
    return self.name