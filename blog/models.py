from django.db import models
from django.db.models.constraints import CheckConstraint
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.query_utils import Q
from django.db.models import F
"""from django.contrib.postgres.fields import ArrayField"""

#Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 320)
    phone = models.CharField(max_length = 12, null = False, blank = False)

class Station(models.Model):
    id = models.IntegerField(default=-1, primary_key = True)
    stationName = models.CharField(max_length = 15)

class Train(models.Model):
    seatNum = models.IntegerField(default=0)
    source = models.ForeignKey(Station, on_delete = models.CASCADE, related_name = "TrainSource",null=False)
    destination = models.ForeignKey(Station, on_delete = models.CASCADE, related_name = "TrainDest",null=False)

    def getSource(self):
        return self.source.id
    def getDest(self):
        return self.destination.id



class Trip(models.Model):
    train = models.ForeignKey(Train, on_delete = models.CASCADE, related_name = "TripTrain")
    source = models.ForeignKey(Station, on_delete = models.CASCADE, related_name = "TripSource", null=False)
    destination = models.ForeignKey(Station, on_delete = models.CASCADE, related_name = "TripDest", null=False)
    day = models.DateField(null = False)
    startTime = models.TimeField(null = False)
    endTime = models.TimeField(null = False)
    price = models.FloatField(null = False, default=0)

    def getSource(self):
        return self.source

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(source__gte = Train.getSource) and models.Q(source__lte = Train.getDest), name="sourceValid"),
            models.CheckConstraint(
                check=models.Q(destination__gte = Train.getSource) and models.Q(destination__lte = Train.getDest), name="destValid")
        ]

class Book(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name = "BookTrips",null = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "BookUser",null = False)
    seats = IntegerField(default=-1)
    class Meta:
        unique_together = (("trip", "user","seats"),)
        
        