from django.shortcuts import render

from rest_framework import generics
from django.contrib.auth import get_user_model 
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class CustomUserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

class CustomUserDetail(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
