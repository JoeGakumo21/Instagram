
from django.shortcuts import render,redirect
from .models import Post
def post(request):
    posts = Post.objects.all().filter
    return render(request,'all-in-one/post.html',{'posts':posts})

def loginPage(request):
    context={}
    return render(request,'all-in-one/login.html', context)

def registerPage(request):
    context={}
    return render(request,'all-in-one/register.html', context)

def NewPost(request):
    posts = Post.objects.all()

    if request.method =='POST':
        data=request.POST
        image=request.FILES.get('image')
        if data['posts'] != 'none':
            posts= Post.objects.get(id=data['category']) 
        elif data['newpost'] != '':
            posts,created=Post.objects.get_or_create(name=data['newpost'])
        else:
            posts=None    
        photo=image.objects.create(
            image=image,
            mycaption=data['mycaption'],
            
        ) 
        return redirect('post')
    context={'posts':posts}
    return render(request, 'all-in-one/newpost.html', context)     