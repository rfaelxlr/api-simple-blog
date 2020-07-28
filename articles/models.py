from django.db import models
from django.contrib.auth import get_user_model

class Article(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.TextField(max_length=200,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.URLField(max_length =300,blank = True)
    content = models.TextField(blank=False)