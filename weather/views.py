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

    context = {
        'city': city,
        'forecast_list': forecast_list,
        'form': form,
    }

    return render(request, 'weather/weather.html', context)
