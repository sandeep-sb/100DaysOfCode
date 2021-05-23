import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

GENDER = 'male'
WEIGHT_KG = 78
HEIGHT_CM = 180
AGE = 22

USERNAME = os.environ.get('USERNAME_')
PASSWORD = os.environ.get('PASSWORD')

API_ID = os.environ.get('API_ID')
API_KEY = os.environ.get('API_KEY')

nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutrition_params = {
    'query': (input('Tell me which exercises you did: ')).title(),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

nutrition_header = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

response = requests.post(url=nutrition_endpoint, json=nutrition_params, headers=nutrition_header)
result = response.json()
print(result)

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

today = datetime.now()
modified_date = today.strftime('%d/%m/%Y')
time = today.strftime('%H: %M: %S')
print(time, modified_date)

sheety_param = None
for exercise in result['exercises']:
    sheety_param = {
        'workout': {
            'Date': modified_date,
            'Time': time,
            'Exercise': exercise['user_input'],
            'Duration': exercise['duration_min'],
            'Calories': exercise['nf_calories'],
        }
    }

sheet_response = requests.post(url=sheety_endpoint, json=sheety_param,
                               auth=HTTPBasicAuth(username=USERNAME, password=PASSWORD))
print(sheet_response.text)
