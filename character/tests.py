from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.
class RaceViewSetTextCase(APITestCase):
    def test_list(self):
        url = reverse('race-list')
        response = self.client.get(url)
        