from rest_framework import serializers
from .models import UserPost

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ['id', 'username', 'created_datetime', 'title', 'content']