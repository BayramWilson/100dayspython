import time
from data_manager import DataManager
from flight_search import FlightSearch

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)
flight_search = FlightSearch()

# ==================== Update the Airport Codes in Google Sheet ====================

# Fetch data from Google Sheet
sheet_data = data_manager.get_destination_data()

# Update IATA codes if needed
for row in sheet_data:
    if row["iataCode"] == "TESTING":  # Or check for an empty string
        row["iataCode"] = flight_search.get_destination_code(row["city"])

# Update the Google Sheet with the new IATA codes
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()