import os 
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

current_time = datetime.datetime.now()
time_hour_minutes = current_time.strftime("%H:%M")
today_date = current_time.strftime("%d.%m.%Y")
# print(current_time)
# print(time_hour_minutes)
# print(today_date)

nutritionix_app_id = os.getenv("NUTRITIONIX_APP_ID")
nutritionix_api_key = os.getenv("NUTRITIONIX_API_KEY")
# print(nutritionix_api_key)
# print(nutritionix_app_id)

nutritionix_url = "https://trackapi.nutritionix.com"
nutritionix_endpoint_natural_exercise = f"{nutritionix_url}/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key,
}

excercise_params = {
    "query": input("Enter your exercise in natural language here: \n")
}
# print(type(excercise_params["query"]))

response = requests.post(url=nutritionix_endpoint_natural_exercise, json=excercise_params, headers=nutritionix_headers )
# print(response.text)

response_data_json = response.json()
# print(response_data_json)

excercise_name = response_data_json["exercises"][0]["name"]
# print(excercise_name)

excercise_duration = response_data_json["exercises"][0]["duration_min"]
# print(excercise_duration)

excercise_calories = response_data_json["exercises"][0]["nf_calories"]
# print(excercise_calories)

sheety_url = "https://api.sheety.co"
sheety_add_row_ep = "https://api.sheety.co/ffc8b9a99ae35d142dc788b0c5a5e26e/myWorkouts/workouts"
sheety_header = {
    "Authorization": os.getenv("SHEETY_AUTH_HEADER")
}

sheety_post_body = {
    "workout": {
        "date": today_date,
        "time": time_hour_minutes,
        "excercise": excercise_name,
        "duration": excercise_duration,
        "calories": excercise_calories
    }
}
post_to_google_sheets = requests.post(url=sheety_add_row_ep, json=sheety_post_body, headers=sheety_header)
print(post_to_google_sheets.text)
