# # from django import forms
# # from django.db.models import fields

# # # from django.forms import widgets
# # from crispy_forms.helper import FormHelper
# # from crispy_forms.layout import Submit,Layout,Field
# # from .models import Post,Comment
# # from django.forms import *
# # from django.contrib.auth.forms import UserCreationForm
# # from django.forms import ModelForm
# # from django.contrib.auth.models import User

# # from myinstagram import models

# # from myinstagram import models

# # 
# from datetime import date, datetime
# from django.contrib.auth import forms
# from django.http import request
# from django.shortcuts import get_object_or_404, render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from .models import Like, Post,Comment, Profile
# from .decorators import unauthenticated_user
# from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm,PostForm,CommentForm
# from django.contrib import messages
# from django .contrib.auth import authenticate, login,logout
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# class PostForm(forms.ModelForm):
#     helper = FormHelper()
#     helper.form_method = 'POST'
#     helper.add_input(Submit('post', 'post',css_class = 'btn btn-success'))

#     class Meta:
#         model = Post
#         fields = [
#             'image',
#             'mycaption'
#         ]

#  #customizing the form
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields =['username','email','password1','password2']


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ['comment_body',]
#         widgets = {
#             'comment_body':forms.Textarea(attrs={'class': 'form-control'}),
#         }



from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from .models import Comment, Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-small btn-success m-4'))
    class Meta:
        model = Post
        fields = [
            'image',
            'mycaption'
        ]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
        widgets = {
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }

