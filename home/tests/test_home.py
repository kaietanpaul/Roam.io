from django.test import RequestFactory, Client
from home.views import home


# Test function to ensure home view returns a 200 status code
def test_home_view_status_code():
    request = RequestFactory().get('/')
    response = home(request)

    assert response.status_code == 200


# Test function to ensure the correct template is used for the home view
def test_home_view_template_used():
    client = Client()
    response = client.get('/')

    assert 'home/home.html' in [t.name for t in response.templates]
