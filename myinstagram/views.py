
from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
def post(request):
    posts = Post.objects.all().filter
    return render(request,'all-in-one/post.html',{'posts':posts})
# login code  goes here
def loginPage(request):
    form= UserCreationForm()
    context={'form':form}
    return render(request,'all-in-one/login.html', context)

def registerPage(request):
    form= UserCreationForm()

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            
    context={'form':form}
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