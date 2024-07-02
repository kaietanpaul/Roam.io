from django.contrib import admin
from .models import Weather, WeatherHour

admin.site.register(Weather)
admin.site.register(WeatherHour)
