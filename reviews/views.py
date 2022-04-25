from django.shortcuts import render
from rest_framework import status
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review

class ReviewCreate(APIView):

  permission_classes = [IsAuthenticated, ]

  def post(self, request):
    request.data['owner'] = request.user.id
    
    try:
      existing_review = Review.objects.get(owner=request.user.id, usage=request.data['usage'])
      if existing_review:
        return Response({'message': 'already rated'})
    except Review.DoesNotExist:
        pass

    review_serializer = ReviewSerializer(data=request.data)
    if review_serializer.is_valid():

      review_serializer.save()

      return Response(data=review_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(data=review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
