from django.db import models


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    likes = models.ImageField(null=True)