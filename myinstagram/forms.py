from django import forms
from django.db.models import fields

from myinstagram.views import post
from .models import Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,Field

from myinstagram import models


class PostForm(forms.ModelForm):
    helper=FormHelper()
    helper.form_method="POST"
    helper.add_input(Submit('Post','post', css_class='btn-primary'))

    class Meta:
        model=post
        fields=[
            'image',
            'mycaption'
        ]