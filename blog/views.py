# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def home_page(request):

    try:
        context = {
            'articles': Article.objects.raw('SELECT * FROM blog_article ORDER BY date DESC'),
        }
    
    except:
        context = {'articles': ''}

    return render(request, "home.html", context)