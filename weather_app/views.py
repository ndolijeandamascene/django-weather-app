import requests
from django.shortcuts import render

def get_weather(request):
    api_key = '7c429a4c27d8171133b31cc8570834eb'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    if request.method == 'POST':
        city = request.POST['city']
        response = requests.get(url.format(city)).json()

        if response['cod'] == 200:
            weather = {
                'city': city,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon']
            }
        else:
            weather = None
    else:
        weather = None

    return render(request, 'weather.html', {'weather': weather})