from django import forms
from django.contrib.auth.models import User
from .models import Profile
from quizSite.forms import MyUserForm,MyForm



# Inheriting from MyForm instead of forms.Form
class SignupForm(MyUserForm):

    user_attrs  = {"placeholder":"username",'autofocus':'','class':'left'}
    email_attrs = {"placeholder":"abc@example.com",'class':'left'}
    pass_attrs  = {"placeholder":"********",'class':'right'}
    
    first_name        = forms.CharField(widget=forms.TextInput({'placeholder':'First Name','autofocus':'autofocus', 'class':'left'}),label='First Name')
    last_name        = forms.CharField(widget=forms.TextInput({'placeholder':'Last Name', 'class':'right'}),label='Last Name')
    username      = forms.CharField(widget=forms.TextInput(user_attrs),label='Username')
    email         = forms.EmailField(widget=forms.TextInput(email_attrs),label='Email')
    password1     = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='Password')
    password2     = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email', 'password1', 'password2']

class ProfileForm(MyForm):

    contrib = forms.BooleanField(label='Do you want to become a cotributer?(Optional)', required=False)

    class Meta:
        model = Profile
        fields = ['contrib']


class LoginForm(MyForm):

    user_attrs  = {"placeholder":"Username"}
    pass_attrs  = {"placeholder":"********"}
    username    = forms.CharField(widget=forms.TextInput(user_attrs),label='Username')
    password    = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='Password')
