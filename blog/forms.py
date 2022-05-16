
from django import forms
from django.forms import ModelForm
from .models import *


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CreateUser(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Enter your password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Confirm password'}),
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1', 'password2']
        widgets={
            'username' : forms.TextInput(attrs={'class':'text-input', 'placeholder':'Enter your username'}),
        }