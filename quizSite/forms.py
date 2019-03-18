from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article


# Overriding the default label suffix(":") included by Django forms
class MyForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super(MyForm,self).__init__(*args, **kwargs)

class MyUserForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super(MyUserForm,self).__init__(*args, **kwargs)


# Inheriting from MyForm instead of forms.Form
class SignupForm(MyUserForm):

    user_attrs  = {"placeholder":"username",'autofocus':''}
    email_attrs = {"placeholder":"abc@example.com"}
    pass_attrs  = {"placeholder":"********"}
    
    f_name        = forms.CharField(widget=forms.TextInput({'placeholder':'First Name','autofocus':'autofocus'}),label='First Name')
    l_name        = forms.CharField(widget=forms.TextInput({'placeholder':'Last Name'}),label='Last Name')
    username    = forms.CharField(widget=forms.TextInput(user_attrs),label='Username')
    email       = forms.EmailField(widget=forms.TextInput(email_attrs),label='Email')
    password1   = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='Password')
    password2   = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='Confirm Password')

    class Meta:
        model = User
        fields = ['f_name', 'l_name','username','email', 'password1', 'password2']

class LoginForm(MyForm):

    user_attrs  = {"placeholder":"Username"}
    pass_attrs  = {"placeholder":"********"}
    username    = forms.CharField(widget=forms.TextInput(user_attrs),label='Username')
    password    = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='Password')

class PostForm(MyForm):
    title_attrs = {"placeholder":"Title", "autofocus":"autofocus"}
    content_attrs = {"placeholder":"Content"}
    title       = forms.CharField(widget=forms.TextInput(title_attrs), label="Title")
    content     = forms.CharField(widget=forms.Textarea(content_attrs), label="Content")
    class Meta:
        model = Article
        fields = ['title', 'content']