from django.urls import path
from .views import UserPostListCreate, UserPostDetail

urlpatterns = [
    path('posts/', UserPostListCreate.as_view(), name='userpost-list-create'),
    path('posts/<int:pk>/', UserPostDetail.as_view(), name='userpost-detail'),
]