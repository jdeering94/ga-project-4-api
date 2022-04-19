from django.urls import path
from songs.views import *

urlpatterns = [
    path('song-list/', SongListCreate.as_view()),
    path('song-detail/<int:pk>/', SongRetrieveUpdateDelete.as_view()),
    path('film-list/', FilmListCreate.as_view()),
    path('film-detail/<int:pk>/', FilmRetrieveUpdateDelete.as_view()),
    path('artist-list/', ArtistListCreate.as_view()),
    path('artist-detail/<int:pk>/', ArtistRetrieveUpdateDelete.as_view()),
    path('album-list/', AlbumListCreate.as_view()),
    path('album-detail/<int:pk>/', AlbumRetrieveUpdateDelete.as_view()),
    path('contexts/', ContextListCreate.as_view()),
    path('context-detail/<int:pk>/', ContextRetrieveUpdateDelete.as_view()),
]