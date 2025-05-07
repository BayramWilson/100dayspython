import requests
LAT=52.520008
LON=13.404954
CNT=4
API_KEY="7c0226413297d612a0941ea07215f315"
URL=f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&cnt={CNT}"
output = requests.get(URL)
print(output.status_code)
weather_data = output.json()
weather_condition_id = weather_data["list"][0]["weather"][0]["id"]
if weather_condition_id < 700:
    print("bring an umbrella!")