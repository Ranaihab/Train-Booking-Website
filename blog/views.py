from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse


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
        return render(request, template, {'form': form, 'errorMsg': 'Email already exists.'})

    else:
        if request.method == "POST":
            user = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('pass')
            )
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            if request.POST.get('isAdmin') == "true":
                user.is_staff = True
                user.is_superuser = True
            else:
                user.is_staff = False
            user.save()
            
            login(request, user)
            return redirect('/')

            # redirect to accounts page:
            #return HttpResponseRedirect('/mymodule/account')
    


def signInForm(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
        else:
            return render(request, 'registrationPages/signIn.html', {'errorMsg': 'Wrong username or password'})



def logOut(request):
    request.session.flush()
    return redirect('/')