# envi\Scripts\activate
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return f"<b>{function()}<b>"

    return bold


def make_emphasis(function):
    def bold():
        return f"<em>{function()}<em>"

    return bold


def make_underline(function):
    def bold():
        return f"<u>{function()}<u>"

    return bold


@app.route("/")  # this is a python decorator
def hello_world():
    return "Hello, World!"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "BYE"


#
#
# @app.route("/<name>")
# def greet(name):
#     return f"hey {name}!"


if __name__ == "__main__":
    app.run(debug=True)
