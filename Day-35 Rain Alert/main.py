import requests
import os
from twilio.rest import Client

MY_LAT = 26.846695
MY_LONG = 80.946167
api_key = '725fa9da724e9c4a1a8587a96e8688e5'
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
account_sid = 'ACcc5d6c90e7caa7fc16e2baef5bbf895b'
auth_token = '57cc6c62ba8b40ac221cdee75845d569'

parameter = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'exclude': 'current,minutely,daily',
    'appid': api_key,
}

response = requests.get(url=OWM_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()

will_rain = False

hourly_data = data['hourly']
for hour in hourly_data[0:12]:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Its going to rain today. Remember to bring an ☔",
        from_='+15302035853',
        to='+91 83036 08402'
    )
    print(message.status)
