from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
#from .forms import RegisterationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


@never_cache
def home(request):
    return render(request, 'sitePages/home.html')


@never_cache
def signIn(request):
    return render(request, 'registrationPages/signIn.html')


@never_cache
def signUp(request):
    return render(request, 'registrationPages/SignUp.html')


@never_cache
def signUpForm(request):
    template = 'registrationPages/signUp.html'

    form = request.POST
    if User.objects.filter(username=request.POST.get('username')).exists(): 
        return render(request, template, {'form': form, 'errorMsg': 'Username is already taken.'})

    elif User.objects.filter(email=request.POST.get('email')).exists(): 
        return render(request, template, {'form': form,'errorMsg': 'Email already exists.'})

    else:
        if request.method =="POST":
            user = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('pass')
            )
            user.fname = request.POST.get('fname')
            user.lname = request.POST.get('sname')
            if request.POST.get('isAdmin') == "true":
                user.is_staff = True
                user.is_superuser = True
            else:
                user.is_staff = False
            user.save()

                #login(request, user)

                # redirect to accounts page:
                #return HttpResponseRedirect('/mymodule/account')
    template = 'sitePages/home.html'
    return render(request, template)
