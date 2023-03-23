from django.db import models


# Represents a weather object containing location and datetime information
class Weather(models.Model):
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.location


# Represents an hourly weather object, temperature, humidity, pressure, and hour, associated with a Weather instance
class WeatherHour(models.Model):
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE, related_name='hours')
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    hour = models.IntegerField()

    def __str__(self):
        return f'{self.weather} at hour {self.hour}'
