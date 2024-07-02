from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from cities.models import City

User = get_user_model()


class WeatherViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    # Tests the weather view, status code, and template used when requesting weather information for a specific city
    def test_weather_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('weather'), {'city': 'New York'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/weather.html')

    # Tests adding a favorite city to the user's profile
    def test_add_favorite_city(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('weather'), {
            'action': 'add',
            'name': 'Paris',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(City.objects.filter(name='Paris').exists())
        self.assertTrue(self.user.favorite_cities.filter(name='Paris').exists())
