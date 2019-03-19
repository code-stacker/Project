from __future__ import print_function
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import LoginForm,SignupForm,PostForm
from .models import Article
from django.contrib import messages


def home_page(request):

    context = {
        'articles': Article.objects.raw('SELECT * FROM quizSite_article ORDER BY date DESC'),
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

@login_required
def new_page(request):
    form = PostForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        messages.success(request, "New post added")
        return redirect('/')

    return render(request, "new_post.html", context)
