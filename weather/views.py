from django.shortcuts import render
from .utils import fetch_weather_data


def weather(request):
    city_name = 'London'
    weather_data = fetch_weather_data(city_name)

    context = {
        'city': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
    }

    return render(request, 'weather/weather.html', context)
