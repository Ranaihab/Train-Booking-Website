from django.contrib import admin
from .models import Station, Train, Trip

admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Trip)