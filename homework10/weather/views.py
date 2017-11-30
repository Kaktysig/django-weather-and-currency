from django.shortcuts import render
import requests

# Create your views here.

def weather (request):
    try:
        url = "http://api.openweathermap.org/data/2.5/find?q=Moscow,RU&APPID=4611941f0036a7d122cc88436e7e4940"
        try:
            json_data = getAPI(url)
        except Exception as e:
            raise ConnectionError

        data = getValues(json_data)

        return render(request, 'weather/index.html', {
            'error' : 'no',
            'full': json_data,
            'data': data,
        })

    except ConnectionError:
        return render(request, 'weather/index.html', {
            'error' : 'Плохое соединение с сервером',
            'oopsmessage' : 'Упс!',
        })


def getAPI(url):
    r = requests.get(url)
    return r.json()

def getValues(json_data):
    data = {}
    data['city'] = json_data['list'][0]['name']
    data['temperature'] = str(int(json_data['list'][0]['main']['temp'] - 273)) + '°'
    data['min_temperature'] = str(int(json_data['list'][0]['main']['temp_min'] - 273)) + '°'
    data['max_temperature'] = str(int(json_data['list'][0]['main']['temp_max'] - 273)) + '°'
    data['weather'] = str(json_data['list'][0]['weather'][0]['main'])
    data['humidity'] = str(json_data['list'][0]['main']['humidity']) + '%'
    return data
