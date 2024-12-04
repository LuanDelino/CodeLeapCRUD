from rest_framework import serializers


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields: ['id', 'username', 'created_datetime', 'title', 'content']
