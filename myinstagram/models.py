from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image=models.ImageField(blank=True, null=True)
    mycaption=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    liked = models.ManyToManyField(User, default=None,blank= True,related_name='liked')
    

    def __str__(self):
        return self.mycaption

    @property
    def num_likes(self):
        return self.liked.all().count    
    @classmethod
    def search_category(cls,search):
            searches = cls.objects.filter(author__username__icontains = search)
            return searches        
        

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=500)
    body=models.TextField()
    date= models.DateTimeField(auto_now_add=True)



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)    

   