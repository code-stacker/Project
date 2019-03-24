# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import SignupForm, ProfileForm
from blog.forms import PostForm

def signup_page(request):
    form = SignupForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    context={"form":form, 'profile':profile_form}
    if form.is_valid() and profile_form.is_valid():
        user = form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        username = form.cleaned_data.get('username')
        messages.success(request, "Account created for {}. Login now!".format(username))
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