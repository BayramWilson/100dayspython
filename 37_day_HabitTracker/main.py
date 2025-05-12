import requests
import os
from dotenv import load_dotenv
import datetime
load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

current_date = datetime.datetime.now()
# print(current_date)

pixela_url = "https://pixe.la"
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

cre_px_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{create_graph["id"]}"

create_pixel = {
    "date": current_date.strftime("%Y%m%d"),
    "quantity": "12",
}

# create_pixel_ep = requests.post(url= cre_px_endpoint, json=create_pixel, headers=headers )

get_user_link = f"{pixela_url}/@{USERNAME}"
print(get_user_link)
# print(create_pixel.text)

update_pixel_ep = f"{pixela_endpoint}/{USERNAME}/graphs/{create_graph["id"]}/{current_date.strftime("%Y%m08")}" 
print(update_pixel_ep)
update_pixel_body = {
    "quantity": "15",
}

# update_pixel = requests.put(url= update_pixel_ep, json=update_pixel_body, headers=headers)
# print(update_pixel.text)

delete_pixel_ep = update_pixel_ep

delete_pixel = requests.delete(url=delete_pixel_ep, headers=headers)
print(delete_pixel.text)