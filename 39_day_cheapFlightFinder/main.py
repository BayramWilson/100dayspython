#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from data_manager import *
from pprint import pprint

sheet_data = getSheetInfo()
# print(sheet_data)
for i in range(2, 11):
    print(i)
    mutSheetInfo(i)
    if i == 10:
        break
