import requests
from django.conf import settings


# Fetches the weather data for a given city name using OpenWeatherMap API and returns the data for the next 3 hours
def fetch_weather_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    data['list'] = data['list'][:3]

    return data
