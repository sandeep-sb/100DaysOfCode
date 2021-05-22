import requests
from datetime import datetime

USERNAME = "sandeepsb"
TOKEN = "fdsibfd3r8r4bi4bf9f92"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading graph",
    "unit": "page",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pix_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pix_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today: "),
}

response = requests.post(url=pix_endpoint, json=pix_config, headers=headers)
print(response.text)

update_pixel_endpoint = f'{pix_endpoint}/{today.strftime("%Y%m%d")}'

update_data = {
    "quantity": input("How many pages did you read today: "),
}

# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f'{pix_endpoint}/{today.strftime("%Y%m%d")}'

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
