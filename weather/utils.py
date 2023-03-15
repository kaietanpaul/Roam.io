import requests
from django.conf import settings


def fetch_weather_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    data['list'] = data['list'][:3]

    return data
