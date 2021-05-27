# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

for data in sheet_data:
    if data['iataCode'] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        data['iataCode'] = flight_search.get_destination_code(data['city'])

pprint(sheet_data)
data_manager.destination_data = sheet_data
data_manager.update_destination_code()

