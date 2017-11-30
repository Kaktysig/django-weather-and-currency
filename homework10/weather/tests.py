from django.test import TestCase
import pytest
import requests

# Create your tests here.

def test_get_api():
    from weather.views import getAPI
    url = "http://api.openweathermap.org/data/2.5/find?q=Moscow,RU&APPID=4611941f0036a7d122cc88436e7e4940"
    answer = getAPI(url)
    right_api = requests.get(url)
    assert right_api == answer