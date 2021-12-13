import requests
from twilio.rest import Client

api_key = "**key**"
MY_LAT = 55.559070
MY_LONG = 37.810622

account_sid = "**sid**"
auth_token = "**token**"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)

response.raise_for_status()
data = response.json()

# 12 hours
next_12_hours = data["hourly"][0:12]

list_of_id = []

will_rain = False

for every_hour in next_12_hours:
    list_of_id.append(every_hour["weather"][0]["id"])

for weather_id in list_of_id:
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Сегодня возможны осадки. Не забудь взять зонт!☂️",
        from_='**number**',
        to='**number'
    )
    print(message.status)
