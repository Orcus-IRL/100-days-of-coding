from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def root():
    return ('<h1 style="text-align:center;">Guess a number between 0 and 9</h1>\n'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style = " margin-left: 38%"><img>')


random_number = randint(0, 9)
print(random_number)


@app.route("/<int:guess>")
def num_guess(guess):
    if guess == random_number:
        return ('<h1 style="text-align:center;color:green;">You guessed it</h1>\n'
                '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style = " margin-left: 38%"><img>')
    elif guess < random_number:
        return ('<h1 style="text-align:center;color:red;">Too Low, try again!</h1>\n'
                '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style = " margin-left: 38%"><img>')
    else:
        return ('<h1 style="text-align:center;color:red;">Too High, try again</h1>\n'
                '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style = " margin-left: 38%"><img>')


if __name__ == "__main__":
    app.run(debug=True)