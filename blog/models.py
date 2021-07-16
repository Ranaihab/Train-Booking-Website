from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date


#Create your models here.
class Seat(models.Model):
    id = models.IntegerField(default=-1, primary_key=True, editable=False)


class Station(models.Model):
    id = models.IntegerField(default=-1, primary_key=True)
    stationName = models.CharField(max_length=15)


class Train(models.Model):
    Number_of_seats = models.IntegerField(default=0)
    source = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="TrainSource", null=False)
    destination = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="TrainDest", null=False)

    def Source(self):
        return self.source.stationName

    def Destination(self):
        return self.destination.stationName

    def clean(self):
        if self.source.id > self.destination.id:
            raise ValidationError("Source and Destination of the train are just 2 end points so kindly enter the source(ID) less than the destination(ID) and if you want the train to move backward choose the desired source and destination in Trips.")

        if self.Number_of_seats <= 19:
            raise ValidationError("Number of seats cannot be less than 20")
        if self.source.id == self.destination.id:
            raise ValidationError("Source and destination cannot be same station")

class Trip(models.Model):
    train = models.ForeignKey(
        Train, on_delete=models.CASCADE, related_name="TripTrain")
    source = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="TripSource", null=False)
    destination = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="TripDest", null=False)
    day = models.DateField(null=False)
    start_Time = models.TimeField(null=False)
    end_Time = models.TimeField(null=False)
    price = models.FloatField(null=False, default=0)
    Remaining_seats = models.IntegerField(default=0, editable=False)
    seats = models.IntegerField(default=0, editable=False)

    def Source(self):
        return self.source.stationName

    def Destination(self):
        return self.destination.stationName

    @property
    def isPast(self):
        return self.day >= date.today()

    def clean(self):
        if self.id is None:
            self.Remaining_seats = self.train.Number_of_seats
            self.seats = self.train.Number_of_seats
        if self.source.id < self.train.source.id or self.source.id > self.train.destination.id:
            raise ValidationError(
                "Source of the trip is not within the route of the train")
        if self.destination.id < self.train.source.id or self.destination.id > self.train.destination.id:
            raise ValidationError(
                "Destination of the trip is not within the route of the train")
        if self.source.id == self.destination.id:
            raise ValidationError(
                "Source and destination cannot be same station")

        trips = Trip.objects.select_related(
            'train').filter(train__id=self.train.id)
        for tr in trips:
            if self.day == tr.day and self.id != tr.id:
                if (self.start_Time >= tr.start_Time and self.start_Time < tr.end_Time) or (self.end_Time > tr.start_Time and self.end_Time <= tr.end_Time):
                    raise ValidationError(
                        "Their is a trip on this train at the same time")
                    break
        if self.start_Time == self.end_Time:
            raise ValidationError(
                "Arrival and departure time cannot be the same time")


class Book(models.Model):
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name="BookTrips", null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="BookUser", null=False)
    seatTrain = models.ManyToManyField(Seat, null=True)
    seats = models.IntegerField(default=0)

    def username(self):
        return self.user.username

