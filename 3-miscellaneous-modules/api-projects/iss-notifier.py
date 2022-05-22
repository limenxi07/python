import requests, smtplib, datetime as dt, time
MY_LAT = 51.270340
MY_LONG = 0.523840

def is_iss_overhead():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()
  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])

  if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    return True

def is_night():
  response = requests.get("https://api.sunrise-sunset.org/json", params={"lat": MY_LAT, "lng": MY_LONG, "formatted": 0,})
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  if dt.now().hour >= sunset or dt.now().hour <= sunrise:
    return True

while True:
  time.sleep(60)
  if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login("email", "password")
      connection.sendmail(from_addr="email", to_addrs="email", msg="Subject:Look up\n\nThe ISS is above you in the sky.")