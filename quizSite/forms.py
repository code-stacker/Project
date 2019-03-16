from django import forms



# Overriding the default label suffix(":") included by Django forms
class MyForm(forms.Form):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super(MyForm,self).__init__(*args, **kwargs)


# Inheriting from MyForm instead of forms.Form
class LoginForm(MyForm):

    email_attrs = {"placeholder":"abc@example.com","type":"text"}
    pass_attrs  = {"placeholder":"********"}
    email       = forms.CharField(widget=forms.TextInput(email_attrs),label='')
    password    = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='')

    def clean_email(self):
        email   = self.cleaned_data.get("email")
        return email
class SignupForm(MyForm):

    name_attrs  = {"placeholder":"Full Name","type":"text"}
    email_attrs = {"placeholder":"abc@example.com","type":"text"}
    pass_attrs  = {"placeholder":"********"}
    name        = forms.CharField(widget=forms.TextInput(name_attrs),label='')
    email       = forms.CharField(widget=forms.TextInput(email_attrs),label='')
    password    = forms.CharField(widget=forms.PasswordInput(pass_attrs),label='')