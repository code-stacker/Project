# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import PostForm

# Create your views here.
def home_page(request):

    try:
        context = {
            'articles': Article.objects.raw('SELECT * FROM blog_article ORDER BY date DESC'),
        }
    
    except:
        context = {'articles': ''}

    return render(request, "home.html", context)


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