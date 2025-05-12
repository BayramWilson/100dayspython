from dotenv import load_dotenv
import os
import requests
load_dotenv()

sheety_api_key = os.getenv("SHEETY_AUTH_HEADER")
headers = {
    "Authorization": sheety_api_key
}
request_body = {
        
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,city,iata,lowestPrice):
        self.city = city
        self.age = iata
        self.lowestPrice = lowestPrice  

def getSheetInfo():
    """This function retrieves the info of Google Sheet"""
    
    retrieve_rows_ep = "https://api.sheety.co/ffc8b9a99ae35d142dc788b0c5a5e26e/flightDeals/prices"
    response = requests.get(url=retrieve_rows_ep, headers=headers)
    return response.text

    
def mutSheetInfo(objID):
     """This function can manipulate the sheet, required is a objectID"""
     
     put_body = {
         "price": {
             "iataCode": "TESTING" #this need title() format
         }
     }
     mut_rows_ep = f"https://api.sheety.co/ffc8b9a99ae35d142dc788b0c5a5e26e/flightDeals/prices/{objID}"
     response = requests.put(url=mut_rows_ep, json=put_body, headers=headers)
     return response.text

    