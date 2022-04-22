from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import UserSerializer
from .user_serializer import CustomUserSerializer
User = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        email = request.data.get('email')
        try:
          existing_user = User.objects.get(email=email)
          if existing_user:
            return Response({'message': 'email already exists'})
        except User.DoesNotExist:
          pass

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=400)


class LoginView(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})
        
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        dt = datetime.now() + timedelta(days=7)

        token = jwt.encode(
          {
            'sub': user.id,
            'exp': int(dt.strftime('%s')),
            'username': user.username
          }, 
          settings.SECRET_KEY, 
          algorithm='HS256'
          )
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})

class CredentialsView(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)


class UpdateUserView(UpdateAPIView):
  queryset = User.objects.all()
  serializer_class = CustomUserSerializer

class AddLikedSong(APIView):
  permission_classes = [IsAuthenticated,]
  def post(self, request):
    songId = request.GET.get('songId')
    user_to_update = self.get_user(pk=request.user.id)
    user_to_update.liked_songs.add(songId)
    user_to_update.save()
    return Response(status=201)



  def get_user(self, pk):
      try:
            return User.objects.get(pk=pk)
      except User.DoesNotExist:
          raise NotFound(detail="Can't find that user")

class RemoveLikedSong(APIView):
  permission_classes = [IsAuthenticated,]
  def put(self, request):
    songId = request.GET.get('songId')
    user_to_update = self.get_user(pk=request.user.id)
    user_to_update.liked_songs.remove(songId)
    user_to_update.save()
    return Response(status=201)

  def get_user(self, pk):
      try:
            return User.objects.get(pk=pk)
      except User.DoesNotExist:
          raise NotFound(detail="Can't find that user")
