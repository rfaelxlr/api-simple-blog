from django.urls import path
from django.conf.urls import include
from articles import views


urlpatterns = [
    path('',views.ArticleListCreate.as_view(),name='LIST E CREATE'),
    path('/<int:pk>',views.ArticleDetail.as_view(),name="GET,UPDATE E DELETE"),    
  
]