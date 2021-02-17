from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def weather_request(request):
    return render(request, 'weather/weather_request.html')


@login_required
def weather_response(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1ea09fd99a6f9eef2b0d5b21af829720'
    city = request.POST['city_name']
    url_response = requests.get(url.format(city)).json()

    context = {
        'title': 'Weather-Response',
        'city': city,
        'temperature': url_response['main']['temp'],
        'description': url_response['weather'][0]['description'],
        'icon': url_response['weather'][0]['icon']
    }
    # print(weather_report)
    return render(request, 'weather/weather_response.html', context)
