from django.shortcuts import render, redirect
from .utils import search_events
from users.forms import FavoriteCitiesForm
from cities.models import City


def events(request):
    user = request.user
    favorite_cities = user.favorite_cities.all()

    all_events = {}
    for city in favorite_cities:
        city_events = search_events(city.name, limit=3)
        all_events[city] = city_events

    if request.method == 'POST' and request.user.is_authenticated:
        action = request.POST.get('action')
        if action == 'edit':
            city_id = request.POST.get('city_id')
            new_city_name = request.POST.get('new_city_name')
            if city_id and new_city_name:
                city = City.objects.get(id=city_id)
                city.name = new_city_name
                city.save()
        elif action == 'delete':
            city_id = request.POST.get('city_id')
            if city_id:
                city = City.objects.get(id=city_id)
                request.user.favorite_cities.remove(city)
                request.user.save()
        return redirect('events')

    return render(request, 'events/events.html', {'events': all_events})
