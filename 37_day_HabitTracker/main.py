import requests
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.json())
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

create_graph = {
    "id": "graph1",
    "name": "My Coding Graph",
    "unit": "Commits",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response_cre = requests.post(url=graph_endpoint, json=create_graph, headers=headers)

# print(response_cre.text)

pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{create_graph["id"]}"

create_pixel