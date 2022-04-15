from django.db import models

class Artist (models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Album (models.Model):
  name = models.CharField(max_length=100)
  image = models.CharField(max_length=200)
  def __str__(self):
    return self.name

class Film (models.Model):
  title = models.CharField(max_length=50)
  Year = models.IntegerField()
  Director = models.CharField(max_length=50)
  image = models.CharField(max_length=200)
  def __str__(self):
    return self.title

class Song (models.Model):
  name = models.CharField(max_length=200)
  films = models.ManyToManyField(Film, related_name='songs', blank=True)
  album = models.ForeignKey(Album, related_name='songs', max_length=100, on_delete=models.CASCADE)
  artist = models.ForeignKey(Artist, related_name='songs', max_length=50, on_delete=models.CASCADE)
  year = models.IntegerField()
  description = models.CharField(max_length=300)
  spotify_link = models.CharField(max_length=200)

  def __str__(self):
    return self.name