from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from .forms import RegisterationForm
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

    form = RegisterationForm(request.POST)
    if form.is_valid():
        if User.objects.filter(username=form.cleaned_data['username']).exists(): 
            return render(request, template, {'form': form, 'errorMsg': 'Username is already taken.'})

        elif User.objects.filter(email=form.cleaned_data['email']).exists(): 
            return render(request, template, {'form': form,'errorMsg': 'Email already exists.'})

        else:
            if request.method == 'POST':
                form = RegisterationForm(request.POST)
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.fname = form.cleaned_data['fname']
                user.lname = form.cleaned_data['lname']
                user.save()

                #login(request, user)

                # redirect to accounts page:
                #return HttpResponseRedirect('/mymodule/account')

    else:
        form = RegisterationForm()

    return render(request, template, {'form': form})
