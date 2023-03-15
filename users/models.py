from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    favorite_cities = models.ManyToManyField('cities.City', blank=True, related_name='favorited_by')
    groups = models.ManyToManyField(Group, blank=True, related_query_name="customuser", related_name="custom_users")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_query_name="customuser", related_name="custom_users")

    def __str__(self):
        return self.username
