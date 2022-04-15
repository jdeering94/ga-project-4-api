from django.urls import path
from songs.views import *

urlpatterns = [
    path('song-list/', SongListCreate.as_view()),
    path('song-detail/<int:pk>/', SongRetrieveUpdateDelete.as_view()),
    path('film-list/', FilmListCreate.as_view()),
    path('film-detail/<int:pk>/', FilmRetrieveUpdateDelete.as_view()),
]