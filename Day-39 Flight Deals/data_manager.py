import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/4c9d528b8443659c28afd8c7a1b0317b/myFlightDeals/prices'

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheet_response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.sheet_data = self.sheet_response.json()
        self.destination_data = self.sheet_data['prices']

    def get_sheet_data(self):
        return self.destination_data

    def update_sheet_data(self):
        for city in self.destination_data:
            data = {
                'price': {
                    'iataCode': city['iataCode'],
                }
            }
            sheety_response = requests.put(url=f'{SHEETY_PRICES_ENDPOINT}/{city["id"]}', json=data)
            print(sheety_response.text)
