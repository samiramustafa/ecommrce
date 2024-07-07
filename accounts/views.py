from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import SingUp_serializer
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated

# Create your views here.

"""
    Expects a POST request with the following data in the request body:
      - first_name (required)
      - last_name (required)
      - email (required, unique)
      - password (required)

    Returns a JSON response with the following:
      - status code:
        - 201 Created: User successfully registered.
        - 400 Bad Request: Validation error or email already in use.

    """

# Registers a new user.

@api_view(['POST'])
def register_user(request):
    if request.method != 'POST':
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    serializer = SingUp_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Use the serializer's save() method for data validation and creation
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# sure about current user.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user=SingUp_serializer(request.user)
    return Response(user.data)