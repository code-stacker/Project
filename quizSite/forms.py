from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Overriding the default label suffix(":") included by Django forms
class MyForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super(MyForm,self).__init__(*args, **kwargs)

class MyUserForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super(MyUserForm,self).__init__(*args, **kwargs)

class MyAuthForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super(MyAuthForm,self).__init__(*args, **kwargs)