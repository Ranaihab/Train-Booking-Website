from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(min_length = 8, max_length = 20)
    email = models.EmailField(max_length = 320)
    phone = models.PhoneNumberField(null = False, blank = False)

class Stations(models.Model):
    id = models.IntegerField(primary_key = True)
    stationName = models.CharField(max_length = 15)

class Train(models.Model):
    seatNum = models.IntegerField()
    source = models.ForeignKey(Stations)
    destination = models.ForeignKey(Stations)

class Trip(models.Model):
    source = models.ForeignKey(Stations)
    destination = models.ForeignKey(Stations)
    train = models.ForeignKey(Train)
    day = models.DateField(null = False)
    time = models.TimeField(null = False)

class Book(models.Model):
    trip = models.ForeignKey(Trip)
    user = models.ForeignKey(User)
    seats = models.

