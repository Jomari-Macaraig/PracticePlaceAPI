from googlemaps import Client

from config.settings import get_key


client = Client(key=get_key('GOOGLE_API_KEY'))


def find_places_ids(query):
    resp = client.places(query)
    results = resp['results']
    places_ids = [place['place_id'] for place in results]
    return places_ids
