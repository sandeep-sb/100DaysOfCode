import requests
import os
from datetime import datetime

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

GENDER = 'male'
WEIGHT_KG = 79
HEIGHT_CM = 180
AGE = 22

nutrix_post_endpooint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutrix_header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

nutrix_param = {
    'query': input('what exercise you did? ').title(),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

print(APP_ID, API_KEY)
response = requests.post(url=nutrix_post_endpooint, json=nutrix_param, headers=nutrix_header)
data_list = response.json()
sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%X')

for nutrix_list in data_list['exercises']:
    sheety_data = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': nutrix_list['name'].title(),
            'duration': nutrix_list['duration_min'],
            'calories': nutrix_list['nf_calories'],
        }
    }

    sheety_header = {
        'Authorization': os.environ.get('AUTHORIZATION'),
        "Content-Type": "application/json",
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_header)
    print(sheety_response.text)
