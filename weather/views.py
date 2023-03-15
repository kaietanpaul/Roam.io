from django.shortcuts import render
from .utils import fetch_weather_data
from datetime import datetime, timedelta


def weather(request):
    city_name = request.GET.get('city', 'Zielona Góra')
    weather_data = fetch_weather_data(city_name)

    city = weather_data['city']['name']
    forecast_list = []

    for index, forecast in enumerate(weather_data['list']):
        current_time = datetime.now()
        hour = (current_time + timedelta(hours=index)).strftime('%H:%M')
        forecast_list.append({
            'hour': hour,
            'temperature': forecast['main']['temp'],
            'humidity': forecast['main']['humidity'],
            'pressure': forecast['main']['pressure'],
        })

    context = {
        'city': city,
        'forecast_list': forecast_list,
    }

    return render(request, 'weather/weather.html', context)
