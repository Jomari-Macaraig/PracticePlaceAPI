from googlemaps import Client

from config.settings import get_key


client = Client(key=get_key('GOOGLE_API_KEY'))


def find_places_ids(query):
    resp = client.places(query)
    results = resp['results']
    places_ids = [place['place_id'] for place in results]
    return places_ids

def get_places_details(places_ids=None):
    FIELDS = [
        'name',
        'website',
        'formatted_address',
        'formatted_phone_number'
    ]
    places_ids = places_ids or []
    for place_id in places_ids:
        result = client.place(
            place_id=place_id,
            fields=FIELDS
        )['result']
        yield {
            'name': result['name'],
            'website': result['website'],
            'formatted_address': result['formatted_address'],
            'formatted_phone_number': result['formatted_phone_number']
        }
