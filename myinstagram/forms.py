from django import forms
from django.db.models import fields
from django.forms import widgets

from myinstagram.views import post
from .models import Post

from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):
    image=forms.ImageField(required=True)
    mycaption= forms.CharField(widget=forms.Textarea,required=True)
    tags=forms.CharField(widgets=forms.TextInput)

    class Meta:
        model=post
        fields =('image','mycaption','tags')