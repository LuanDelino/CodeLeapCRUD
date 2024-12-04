from rest_framework import generics
from .models import UserPost
from .serializers import UserPostSerializer

class UserPostListCreate(generics.ListCreateAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class UserPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
