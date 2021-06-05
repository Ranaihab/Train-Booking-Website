from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

@never_cache
def home(request):
    return render(request, 'sitePages/home.html')

@never_cache
def signIn(request):
    return render(request, 'registrationPages/signIn.html')

@never_cache
def signUp(request):
    return render(request, 'registrationPages/SignUp.html')