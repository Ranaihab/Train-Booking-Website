from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


#Create your models here.
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
    Remaining_seats = models.IntegerField(default=0)

    def Source(self):
        return self.source.stationName

    def Destination(self):
        return self.destination.stationName

    def clean(self):
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
            if self.day == tr.day:
                if (self.start_Time >= tr.start_Time and self.start_Time < tr.end_Time) or (self.end_Time > tr.start_Time and self.end_Time <= tr.end_Time):
                    raise ValidationError(
                        "Their is a trip on this train at the same time")
                    break


class Book(models.Model):
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name="BookTrips", null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="BookUser", null=False)
    seats = IntegerField(default=-1)

    class Meta:
        unique_together = (("trip", "user", "seats"),)

