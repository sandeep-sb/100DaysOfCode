import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/4c9d528b8443659c28afd8c7a1b0317b/myFlightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            updated_data = {
                'price': {
                    'iataCode': city['iataCode'],
                }
            }
            response = requests.put(url=f'{SHEETY_PRICES_ENDPOINT}/{city["id"]}', json=updated_data)
            print(response.text)
