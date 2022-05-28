import requests
from twilio.rest import Client
account_sid = 'placeholder'
auth_token = 'placeholder'
EMAIL = 'placeholder'

weather_params = {
  "lat": 51.507351,
  "lon": -0.127758,
  "appid": "api_key",
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
will_rain = False

for hour in weather_slice:
  code = hour["weather"][0]["id"]
  if int(code) < 700:
    will_rain = True

if will_rain:
  client = Client(account_sid, auth_token)
  message = client.messages.create(
      body="It's going to rain today. Remember to bring an umbrella.",
      from_ = EMAIL,
      to=EMAIL
  )
  print(message.status)
