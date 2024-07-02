from django.shortcuts import render, redirect
from .utils import search_events
from users.forms import FavoriteCitiesForm
from cities.models import City


# View function handling event search and display for authenticated users with favorite cities
# and unauthenticated users with a provided city name
def events(request):
    city_name = request.GET.get('city', None)

    if request.user.is_authenticated:
        user = request.user
        favorite_cities = user.favorite_cities.all()

        all_events = {}
        for city in favorite_cities:
            city_events = search_events(city.name, limit=3)
            all_events[city] = city_events

        if request.method == 'POST':
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

    else:
        if city_name:
            city_events = search_events(city_name, limit=3)
        else:
            city_events = []
        return render(request, 'events/events.html', {'city_events': city_events})
