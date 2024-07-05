from flask import Flask, render_template
from random import randint
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def root():
    random_number = randint(1, 10)
    year = datetime.date.today().year
    return render_template("index.html", num=random_number, curr_year=year)


@app.route("/guess/<string:enter_name>")
def game(enter_name):
    age_response = requests.get(f'https://api.agify.io?name={enter_name}')
    gender_response = requests.get(f'https://api.genderize.io?name={enter_name}')
    return render_template("index.html", name=enter_name,
                           age=str(age_response.json()["age"]),
                           gender=gender_response.json()["gender"])


if __name__ == "__main__":
    app.run(debug=True)
