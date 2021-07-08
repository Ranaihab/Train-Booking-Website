from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
"""from django.contrib.postgres.fields import ArrayField"""

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 320)
    phone = models.CharField(max_length = 12, null = False, blank = False)

class Stations(models.Model):
    id = models.IntegerField(primary_key = True)
    stationName = models.CharField(max_length = 15)

class Train(models.Model):
    seatNum = models.IntegerField(null=False)
    source = models.ForeignKey(Stations, on_delete = models.CASCADE, related_name = "TrainSource",null=False)
    destination = models.ForeignKey(Stations, on_delete = models.CASCADE, related_name = "TrainDest",null=False)


class Trip(models.Model):
    source = models.ForeignKey(Stations, on_delete = models.CASCADE, related_name = "TripSource", null=False)
    destination = models.ForeignKey(Stations, on_delete = models.CASCADE, related_name = "TripDest", null=False)
    
    train = models.ForeignKey(Train, on_delete = models.CASCADE, related_name = "TripTrain")
    day = models.DateField(null = False)
    startTime = models.TimeField(null = False)
    endTime = models.TimeField(null = False)

class Book(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name = "BookTrips",null = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "BookUser",null = False)
    seats = IntegerField(default=-1)
    class Meta:
        unique_together = (("trip", "user","seats"),)