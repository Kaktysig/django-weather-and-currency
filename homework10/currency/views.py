from django.shortcuts import render
import requests

# Create your views here.

def currency (request):
    try:
        data = getValues()

        return render(request, 'currency/index.html', {
            'error' : 'no',
            'data': data,
        })

    except ConnectionError:
        return render(request, 'currency/index.html', {
            'error' : 'Плохое соединение с сервером',
            'oopsmessage' : 'Упс!',
        })


def getAPI(url):
    r = requests.get(url)
    return r.json()

def getValues():
    url = "https://api.fixer.io/latest?base=USD&symbols=RUB"
    try:
        json_usd = getAPI(url)
    except Exception as e:
        raise ConnectionError

    url = "https://api.fixer.io/latest?base=EUR&symbols=RUB"
    try:
         json_eur = getAPI(url)
    except Exception as e:
        raise ConnectionError

    data = {}
    data['usd'] = str(json_usd['rates']['RUB']) + " ₽"
    data['eur'] = str(json_eur['rates']['RUB']) + " ₽"
    return data
