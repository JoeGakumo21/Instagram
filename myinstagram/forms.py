from django import forms
from django.db.models import fields
# from django.forms import widgets
from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field
from .models import Post

from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
from django.contrib.auth.models import User

# from myinstagram import models

# 

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-success'))

    class Meta:
        model = Post
        fields = [
            'image',
            'mycaption'
        ]

 #customizing the form
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']


