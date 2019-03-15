from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm,SignupForm


def home_page(request):
    return render(request, "base.html", {})

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form":form}
    # if request.method == "POST":
    #     print "Email: ", request.POST.get("email")
    #     print "Pass: ", request.POST.get("password")
    if form.is_valid():
        print ("Email",form.cleaned_data.get("email"))
        print ("Pass", form.cleaned_data.get("password"))
    return render(request, "login.html", context)



def signup_page(request):
    form = SignupForm(request.POST or None)
    context={"form":form}
    # if request.method == "POST":
    #     print "Email: ", request.POST.get("email")
    #     print "Pass: ", request.POST.get("password")
    if form.is_valid():
        print (form.cleaned_data)

    return render(request, "signup.html", context)