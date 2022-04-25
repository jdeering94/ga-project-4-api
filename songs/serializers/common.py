from rest_framework import serializers

# from jwt_auth.models import CustomUser
from jwt_auth.serializers import UserSerializer
from reviews.serializers import ReviewSerializer
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

  artist = ArtistSerializer()
  album = AlbumSerializer()
  films = FilmSerializer(many=True)
  liked_by = UserSerializer(many=True)
  

class SongWithoutFilmInfo(SongSerializer):
  artist = ArtistSerializer()
  album = AlbumSerializer()

class PopulatedFilmSerializer(FilmSerializer):
  songs = SongWithoutFilmInfo(many=True)

class PopulatedAlbumSerializer(AlbumSerializer):
  songs = SongSerializer(many=True)

class PopulatedArtistSerializer(ArtistSerializer):
  songs = PopulatedSongSerializer(many=True)

class ContextSerializer(serializers.ModelSerializer):
    class Meta:
      model = Context
      fields = ('__all__')

class PopulatedContextSerializer(ContextSerializer):
  song = SongSerializer()
  film = FilmSerializer()