from django.db import models
from cities.models import City


class Event(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.title
