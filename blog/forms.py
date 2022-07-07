
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'category', 'cover']
        widgets={
            'title' : forms.TextInput(attrs={'class':'text-input', 'placeholder':'Enter task here'}),
            'desc' : forms.Textarea(attrs={'class':'text-input'}),
            'category' : forms.Select(attrs={'class':'text-input'}),
        }

class CreateUser(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Enter your password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Confirm password'}),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'text-input', 'placeholder':'Enter your Email'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder':'Enter your username'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder':'First Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder':'Last Name'})
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1', 'password2']
    

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists() and email !="":
            raise forms.ValidationError("Email is already used")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Password don\'t match")
        return password2