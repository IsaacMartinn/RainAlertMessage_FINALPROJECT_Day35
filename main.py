import requests
from twilio.rest import Client

ACCOUNT_SID = "AC68b4278528e0c8b4d69a6f1f4d4f5818"
AUTH_TOKEN = "84b4663244ff197c97d766e2416450e2"

API_KEY = "1321b6d34e9f257b7968f1c35b6f3176"
MY_LAT = 43.972519
MY_LONG = -79.247063

parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])
list_of_condition = []

will_rain = False

for hour_data in weather_data['list']:
    condition_code = (hour_data['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID,AUTH_TOKEN)

    message = client.messages.create(
        from_="+14142553271",
        to="+14168852667",
        body="It's going to rain today. Remember to bring an ☔️"
    )
print(message.sid)