
from django import forms
from django.forms import ModelForm
from .models import *
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'category', 'author', 'cover']
        widgets={
            'title' : forms.TextInput(attrs={'class':'text-input', 'placeholder':'Enter task here'}),
            'desc' : forms.Textarea(attrs={'class':'text-input'}),
            'category' : forms.Select(attrs={'class':'text-input'}),
            'author' : forms.TextInput(attrs={'class':'text-input', 'placeholder':'Enter task here'}),
        }