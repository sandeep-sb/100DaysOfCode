from pprint import pprint
import requests

KIWI_API = 'https://tequila-api.kiwi.com/locations/query'


class FlightSearch:
    def get_destination_code(self, city_name):
        parameters = {
            'term': city_name,
            'location_types': 'city',
        }
        header = {
            'apikey': 'M8BPAdzcrAQiErCyDk0nCiK775Sl7Ti1',
        }
        response = requests.get(url=KIWI_API, params=parameters, headers=header)
        result = response.json()['locations']
        code = result[0]['code']
        return code
