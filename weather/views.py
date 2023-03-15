from django.shortcuts import render


def weather(request):
    return render(request, 'weather/weather.html')
