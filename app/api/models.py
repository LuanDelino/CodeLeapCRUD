from django.db import models


class UserPost(models.Model):
    id = models.IntegerField()
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
