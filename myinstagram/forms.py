from django import forms
from django.db.models import fields
# from django.forms import widgets
from django.forms.models import ModelForm

from .models import Post

from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
from django.contrib.auth.models import User

# from myinstagram import models

# class NewPostForm(forms.ModelForm):
#     image=forms.ImageField(required=True)
#     mycaption= forms.CharField(widget=forms.Textarea,required=True)
#     tags=forms.CharField(widgets=forms.TextInput)

#     class Meta:
#         model=Post
#         fields =('image','mycaption','tags')


 #customizing the form
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']


