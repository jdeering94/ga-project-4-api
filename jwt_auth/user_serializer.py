from rest_framework import serializers
from django.contrib.auth import get_user_model
from reviews.serializers import PopulatedReviewSerializer
from songs.serializers.common import PopulatedSongSerializer

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
  liked_songs = PopulatedSongSerializer(many=True)
  reviews = PopulatedReviewSerializer(many=True)
  class Meta:
    model = User
    fields = ('username', 'image', 'liked_songs', 'reviews')