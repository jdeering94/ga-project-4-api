from rest_framework import serializers
from ..models import *

class SongSerializer(serializers.ModelSerializer):

  class Meta:
    model = Song
    fields = ('__all__')

class FilmSerializer(serializers.ModelSerializer):

    class Meta:
      model = Film
      fields = ('__all__')

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
      model = Artist
      fields = ('__all__')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
      model = Album
      fields = ('__all__')

class PopulatedSongSerializer(SongSerializer):

  films = FilmSerializer(many=True)
  artist = ArtistSerializer()
  album = AlbumSerializer()

class SongWithoutFilmInfo(SongSerializer):
  artist = ArtistSerializer()
  album = AlbumSerializer()

class PopulatedFilmSerializer(FilmSerializer):
  songs = SongWithoutFilmInfo(many=True)
