from django.contrib import admin
from .models import Station, Train, Trip

class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'stationName')
class TrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'Source', 'Destination', 'Number_of_seats')
class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'train', 'Source', 'Destination', 'day', 'start_Time', 'end_Time', 'price', 'Remaining_seats')
admin.site.register(Station, StationAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Trip, TripAdmin)