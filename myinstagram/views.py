
from django.shortcuts import render
from .models import Post

def post(request):
    posts = Post.objects.all().filter
    return render(request,'all-in-one/post.html',{'posts':posts})