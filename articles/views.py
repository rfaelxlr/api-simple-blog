from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class= ArticleSerializer
   
    
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
