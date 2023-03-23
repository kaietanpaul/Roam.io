from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from events.views import events
from cities.models import City
from users.models import User
import pytest


@pytest.fixture
def city():
    return City.objects.create(name="New York")


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="testpassword")


# Test if events view is accessible by an unauthenticated user without showing city events
@pytest.mark.django_db
def test_events_view_not_authenticated(city):
    request = RequestFactory().get('/events/')
    request.user = AnonymousUser()

    response = events(request)

    assert response.status_code == 200
    assert "New York" not in response.content.decode()


# Test if events view is accessible by an authenticated user and shows city events
@pytest.mark.django_db
def test_events_view_authenticated(user, city):
    request = RequestFactory().get('/events/')
    request.user = user
    user.favorite_cities.add(city)

    response = events(request)

    assert response.status_code == 200
    assert "New York" in response.content.decode()

