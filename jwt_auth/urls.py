from django.urls import path
from jwt_auth.views import *

urlpatterns = [    
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('users/<int:pk>/', UpdateUserView.as_view()),
    path('users/add-liked-song/', AddLikedSong.as_view()),
    path('users/remove-liked-song/', RemoveLikedSong.as_view()),
]