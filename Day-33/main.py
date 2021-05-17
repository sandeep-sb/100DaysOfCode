import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
MY_EMAIL = "sandeepsbhadouria@gmail.com"
MY_PASSWORD = "1234567"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def close_to_iss():
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


def email_send():
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                        msg="Subject:ISS passing by\n\nLook up to see ISS")
    connection.close()


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


# If the ISS is close to my current position
while True:
    time.sleep(60)
    if close_to_iss() and (sunrise > time_now.hour > sunset):
        email_send()
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
