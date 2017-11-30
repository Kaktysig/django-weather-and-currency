from django.test import TestCase
import requests

# Create your tests here.


class TestViews(TestCase):
    def test_get_api(self):
        response = self.client.get('/weather/')
        self.assertEquals(response.status_code, 200)