from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):
    def test_page_is_working(self):
        response = self.client.get('/weather/')
        self.assertEquals(response.status_code, 200)