
from django.shortcuts import render
from .models import Post
from django.forms import NewPostForm
def post(request):
    posts = Post.objects.all().filter
    return render(request,'all-in-one/post.html',{'posts':posts})

def NewPost(request):
    tags_objs=[]
    if request.method=="POST":
        form=NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            image=form.cleaned_data.get('image')
            mycaption=form.cleaned_data.get('mycaption')
            tags_form=form.cleaned_data.get('tags')
