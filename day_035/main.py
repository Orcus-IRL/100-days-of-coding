import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your api key"

weather_params = {
    "lat" : 10.930405,
    "lon" : 76.998542,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"

}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_Data = response.json()
hourly = weather_Data["hourly"][0:12]

will_rain = False
for i in hourly:
    id_codes = i["weather"][0]["id"]
    if id_codes <700:
        # print(f"{id_codes}--->Bring an Umbrella")
        will_rain = True
if will_rain:
    print("Bring an umbrella")
