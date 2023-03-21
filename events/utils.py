import requests

API_ENDPOINT = 'https://app.ticketmaster.com/discovery/v2/events.json'


def search_events(city, keyword=None, limit=3):
    params = {
        'apikey': '7otU1YLIy2o8tctOhbTgOiJgphKUNGHK',
        'city': city,
        'size': limit,
    }

    if keyword:
        params['keyword'] = keyword

    try:
        response = requests.get(API_ENDPOINT, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            print("API limit reached. Please try again later.")
        else:
            print(f"An error occurred while fetching events: {e}")
        return []

    data = response.json()

    if '_embedded' in data:
        return data["_embedded"]["events"]
    else:
        return []
