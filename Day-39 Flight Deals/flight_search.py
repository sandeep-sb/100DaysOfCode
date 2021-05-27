import requests

API_Key = 'M8BPAdzcrAQiErCyDk0nCiK775Sl7Ti1'
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.iata = None
        self.return_iata()

    def return_iata(self):
        return self.iata

    def search_iata(self):
        header = {
            'apikey': API_Key,
        }

        data = {
            'term': self.city,
            'location_types': 'city',
        }
        flight_response = requests.get(url=TEQUILA_ENDPOINT, params=data, headers=header)
        flight_data = flight_response.json()
        print(flight_data)
        self.return_iata()
