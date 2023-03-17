from django.shortcuts import render
from .utils import fetch_weather_data
from datetime import datetime, timedelta
from users.forms import FavoriteCitiesForm
from users.models import User
from cities.models import City


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

    if request.method == 'POST' and request.user.is_authenticated:
        form = FavoriteCitiesForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data.get('name')
            city, created = City.objects.get_or_create(name=city_name)
            request.user.favorite_cities.add(city)
            request.user.save()
    else:
        form = FavoriteCitiesForm()

    favorite_cities = []
    favorite_cities_data = []

    if request.user.is_authenticated:
        favorite_cities = request.user.favorite_cities.all()
        for fav_city in favorite_cities:
            fav_city_weather_data = fetch_weather_data(fav_city.name)
            fav_city_forecast_list = []

            for index, forecast in enumerate(fav_city_weather_data['list']):
                current_time = datetime.now()
                hour = (current_time + timedelta(hours=index)).strftime('%H:%M')
                fav_city_forecast_list.append({
                    'hour': hour,
                    'temperature': forecast['main']['temp'],
                    'humidity': forecast['main']['humidity'],
                    'pressure': forecast['main']['pressure'],
                })
            favorite_cities_data.append({
                'city': fav_city,
                'list': fav_city_forecast_list
            })

    context = {
        'city': city,
        'forecast_list': forecast_list,
        'form': form,
        'favorite_cities': favorite_cities,
        'favorite_cities_data': favorite_cities_data,
    }

    return render(request, 'weather/weather.html', context)
