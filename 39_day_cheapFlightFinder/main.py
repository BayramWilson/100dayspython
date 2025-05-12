#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

sheety_api_key = os.getenv("SHEETY_AUTH_HEADER")

pprint(sheety_api_key)