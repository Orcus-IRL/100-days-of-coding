import requests
import datetime

APP_ID = "your app id"
API_KEY = "your api key"
weight = 75
height = 167
age = 21
query = input("Enter the exercise you did: ")

url_enpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise?{query}"
sheety_endpoint = "https://api.sheety.co/ee7798175747fa89b6210f3172fecbaa/myWorkouts/workouts"

header = {
    'Content-Type': 'application/json',
    'x-app-id':APP_ID ,
    'x-app-key': API_KEY
  }


query_params = {
    "query":query,
    "weight_kg": weight,
    "height_cm":height,
    "age":age
}

response = requests.post(url=url_enpoint,headers=header,json=query_params)
result = response.json()
# print(result)

today_date = datetime.date.today().strftime("%d/%m/%Y")
today_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
        "date":today_date,
        "time": today_time,
        "exercise": exercise['name'].title(),
        "duration":exercise["duration_min"],
        "calories":exercise["nf_calories"] 
        }
    }

authentication = {
    "Authorization":"Bearer qwertyasdfgzxcv"
}
    

sheet_response = requests.post(url=sheety_endpoint,json=sheet_input,headers=authentication)
print(sheet_response.text)
