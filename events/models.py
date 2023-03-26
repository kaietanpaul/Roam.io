from django.db import models
from cities.models import City


# Event model representing an event with a title, date, and associated city
class Event(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.title
