import requests
from datetime import date

today_date = str(date.today()).replace("-", "")
# date(year=2024,month=1,day=08)


my_account = "https://pixe.la/@username"
token = "your token"
username = "user name"
graph_id = "graph"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs/"
pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today_date}"
delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/20240108"

headers = {
    "X-USER-TOKEN": token
}

# Creating a pixela account
user_params = {
    "token": token,
    "username": username,
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}
account_Create_response = requests.post(url=pixela_endpoint, json=user_params)
# print(account_Create_response.text)


# Creating a graph
graph_config = {
    "id": graph_id,
    "name": "Coding graph",
    "unit": "hour",
    "type": "int",
    "color": "shibafu"
}
graph_create_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_create_response.text)


# pixelating the hours of coding done on that day
pixel_config = {
    "date": today_date,
    "quantity": "6"
}
pixel_creation_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_creation_response.text)


# UPDATING PREVIOUS DAY CODING HOUR
update_params = {
    "quantity": "4"
}
update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update_response.text)


# DELETING A PIXEL
delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel_response.text)
