from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image=models.ImageField(blank=True, null=True)
    mycaption=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.mycaption

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    date= models.DateTimeField(auto_now_add=True)