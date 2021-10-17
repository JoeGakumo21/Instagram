
from django.shortcuts import render,redirect
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
            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                t, created=tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
                p, created=Post.objects.get_or_create(image=image, mycaption=mycaption)
                p.tags.set(tags_objs)
                p.save()
                return  redirect('post')

    else:
        form=NewPostForm()
    context={
        'form':form
    }  
    return render(request, 'all-in-one/newpost.html', context)  