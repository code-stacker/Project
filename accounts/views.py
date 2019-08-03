# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignupForm, ProfileForm

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
        messages.success(request, f"Account created for {username}. Login now!")
        return redirect('/login')

    return render(request, "signup.html", context)
