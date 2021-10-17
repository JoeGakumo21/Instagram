
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import CreateUserForm,PostForm,CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
def post(request):

    posts = Post.objects.all().filter(created_date__lte = timezone.now()).order_by('-created_date')
    user = request.user
    comments=Comment.objects.filter(post=posts).order_by('date')


    # comment form
    if request.method== "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comments=form.save(commit=False)
            comments.posts=posts
            comments.user=user
            comments.save()
            return HttpResponseRedirect(reversed('post',))
        else:
            form=CommentForm()
            

    return render(request,'all-in-one/post.html',{'posts':posts,'user':user})
    
   
# login code  goes here
def loginPage(request):
    # form= UserCreationForm()
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')


        user=authenticate(request,username=username, password=password )
        
        if user is not None:
            login(request, user)
            return redirect('post')
        else:
            messages.warning(request,'Username Or Password is incorrect') 
    


    context={}
    return render(request,'all-in-one/login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form= CreateUserForm()

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            holdeofaccount=form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+ holdeofaccount)
            return redirect('login')


    context={'form':form}
    return render(request,'all-in-one/register.html', context)

def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('postview')
    else:
        form = PostForm()
    return render(request,'all-in-one/newpost.html',{'form':form})   