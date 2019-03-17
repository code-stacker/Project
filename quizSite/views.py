from __future__ import print_function
from django.shortcuts import render,redirect
from .forms import LoginForm,SignupForm,PostForm
from .models import Article
from django.contrib import messages


def home_page(request):

    context = {
        'articles': Article.objects.all(),
    }

    return render(request, "home.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form":form}
    # if request.method == "POST":
    #     print "Email: ", request.POST.get("email")
    #     print "Pass: ", request.POST.get("password")
    if form.is_valid():
        print ("Email",form.cleaned_data.get("email"))
        print ("Pass", form.cleaned_data.get("password1"))
    return render(request, "login.html", context)



def signup_page(request):
    form = SignupForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, "Account created for {}. Login now!".format(user))
        return redirect('/login')

    return render(request, "signup.html", context)


def new_page(request):
    form = PostForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        form.save()
        messages.success(request, "New post added")
        return redirect('/')

    return render(request, "new_post.html", context)
