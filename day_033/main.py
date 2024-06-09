import requests
from datetime import datetime


my_lat = 
my_long = 
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_positons = (latitude,longitude)
# print(iss_positons)

parameter = {
    "lat": my_lat,
    "long": my_long,
    "formatted"  : 0
}

response = requests.get(url=" https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(datetime.now().hour)
