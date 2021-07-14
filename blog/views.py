from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Book, Station, Trip, Seat
from django.core import serializers
import json
from datetime import date, datetime

@never_cache
def home(request):
    trips = Trip.objects.all()
    stations = Station.objects.all()
    tripJSON = serializers.serialize("json",trips)
    tripObj = json.loads(tripJSON)
    return render(request, 'sitePages/home.html', {'trips': trips, 'stations': stations, 'data': json.dumps(list(tripObj))})


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
            return render(request, 'registrationPages/signIn.html', {'errorMsg': 'Wrong username or password'})



def logOut(request):
    request.session.flush()
    return redirect('/')

def updateProfile(request):

    """if request.is_ajax:
        if request.method =="POST":
            user=User.objects.filter(id= request.POST['userId'])
        if user.username!=data['username']:
            if User.objects.filter(username= request.POST['username']).exists():
                return JsonResponse({'msg': 'Username is already taken.'})
            else:
                user.username=request.POST['username']

        if user.email!=request.POST['email']:
            if User.objects.filter(email=request.POST['email']).exists():
                return JsonResponse({'msg': 'Email is already taken.'})
            else:
                user.email=request.POST['email']
        if user.first_name!=request.POST['fname']: 
            user.first_name=request.POST['fname'] 
        if user.last_name!=request.POST['lname']: 
            user.last_name=request.POST['lname']  
        if user.password!=request.POST['password']: 
            user.password=request.POST['password']       
        user.save() 
        return JsonResponse({'msg':"Information Saved"})"""

    if request.is_ajax:
        if request.method =="POST":
           
            data = json.loads(request.body)

            user=User.objects.get(id= data['userId'])

            if user.username!=data['username']:
                
                if User.objects.filter(username= data['username']).exists():
                    return JsonResponse({'msg': 'Username is already taken.'})
                else:
                    user.username=data['username']

            if user.email!=data['email']:
                if User.objects.filter(email=data['email']).exists():
                    return JsonResponse({'msg': 'Email is already taken.'})
                else:
                    user.email=data['email']
            if user.first_name!=data['fname']: 
                user.first_name=data['fname'] 
            if user.last_name!=data['lname']: 
                user.last_name=data['lname']  
            if user.password!=data['password']: 
                user.password=data['password']      
            user.save()
            return JsonResponse({'msg':"Information Saved"})
              


def profile(request, username):
    return render(request, "sitePages/profile.html", {'username': username})

def myTrips(request, id):
    book = Book.objects.filter(user = id)
    return render(request, "sitePages/myTrips.html", {'books': book})

def cancelBook(request):
    if request.is_ajax:
        if request.method =="GET":
            bookId = request.GET['bookId']
            userId = request.GET['userId']
            obj = Book.objects.filter(id=bookId)
            trip = obj[0].trip
            if trip.day < date.today() or (trip.day == date.today() and trip.start_Time <= datetime.now().strftime("%I:%M %p")):
                return JsonResponse({'msg':"Trip time has passed cannot cancel"})
            bookSeats = obj.values_list('seatTrain', flat=True)
            seatCount = len(bookSeats)
            trip.Remaining_seats += seatCount
            trip.save()
            obj.delete()   
            return JsonResponse({'msg':"Book is canceled"})

def certainTrip(request, id):
    if request.user.is_authenticated:
        trip = Trip.objects.get(id = id)

        return render(request, 'sitePages/certainTrip.html', {'trip': trip})
    else:
        trips = Trip.objects.all()
        return render(request, 'sitePages/home.html', {'errorMsg': 'Please sign in or sign up to book', 'trips': trips})

def book(request):
    if request.method == "POST":
        tid = request.POST.get('tripId')
        if(tid is None):
            return render
        trip = Trip.objects.get(id = tid)
        book = Book(
                trip = trip,
                user = request.user,
                seats = len(request.POST.get('selected')),
            )
        book.save()
        
        for i in request.POST.getlist('selected'):
            if not Seat.objects.filter(id = i):
                seat = Seat(id = i)
                seat.save()
            seat = Seat.objects.get(id = i)
            book.seatTrain.add(seat)
            trip.Remaining_seats -= 1
            trip.save()
        book.save()
        trips = Trip.objects.all()
        return render(request, 'sitePages/Home.html', {'errorMsg': 'Book is successful', 'trips': trips})
