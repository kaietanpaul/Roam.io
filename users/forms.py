from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from cities.models import City


# Custom user registration form with additional email field
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Form for adding favorite cities to user profile
class FavoriteCitiesForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
