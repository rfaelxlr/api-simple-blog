from django.urls import path
from django.conf.urls import include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users',views.CustomUserList.as_view(),name='LIST E CREATE'),
    path('users/<int:pk>',views.CustomUserDetail.as_view(),name="GET,UPDATE E DELETE"),    
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
