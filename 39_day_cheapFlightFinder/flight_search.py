import os
from dotenv import load_dotenv
import requests

load_dotenv()



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
    
    def _get_new_token(self):
        headers={
        "Content-Type": "application/x-www-form-urlencoded"
        }

        data={
        "grant_type": "client_credentials",
        "client_id": self._api_key,
        "client_secret": self._api_secret
        }

        endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        response = requests.post(url=endpoint, headers=headers, data=data)

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
