import smtplib
import time

import requests
from datetime import datetime

MY_LAT = # Your latitude
MY_LONG = # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    # If the ISS is close to my current position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login("livewithpurpose007@gmail.com", "avk123avk/avk")
        connection.sendmail(
            from_addr="livewithpurpose007@gmail.com",
            to_addrs="livewithpurpose007@gmail.com",
            msg="Look up \n The ISS is above you in the sky"
        )
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
