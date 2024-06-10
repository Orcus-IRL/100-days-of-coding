
import requests
import random
parameter = {
    "amount" : 10,
    "type" : "boolean"
}
response = requests.get(url="https://opentdb.com/api.php",params=parameter)
response.raise_for_status()
data = response.json()
select_question = random.randint(1,10)
question_data = data["results"]



























