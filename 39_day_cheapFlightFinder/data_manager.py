import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ffc8b9a99ae35d142dc788b0c5a5e26e/flightDeals/prices"

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"  # Replace with your token
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        data = response.json()
        self.destination_data = data.get("prices", [])  # Use .get() to avoid KeyError
        return self.destination_data

    def update_destination_codes(self):
        headers = {
            "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"  # Include the Bearer token
        }
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]  # Use the updated IATA code
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

# def getSheetInfo():
#     """This function retrieves the info of Google Sheet"""
    
#     retrieve_rows_ep = "https://api.sheety.co/ffc8b9a99ae35d142dc788b0c5a5e26e/flightDeals/prices"
#     response = requests.get(url=retrieve_rows_ep, headers=headers)
#     return response.text

    
# def mutSheetInfo(objID):
#      """This function can manipulate the sheet, required is a objectID"""
     
#      put_body = {
#          "price": {
#              "iataCode": "TESTING" #this need title() format
#          }
#      }
#      mut_rows_ep = f"https://api.sheety.co/ffc8b9a99ae35d142dc788b0c5a5e26e/flightDeals/prices/{objID}"
#      response = requests.put(url=mut_rows_ep, json=put_body, headers=headers)
#      return response.text

