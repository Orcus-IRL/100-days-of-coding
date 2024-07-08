import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from flask import Flask, render_template, request
import requests
MY_EMAIL = os.environ.get('email')
MY_PASSWORD = os.environ.get('password')

all_posts = requests.get("https://api.npoint.io/edf412412fe96fde65fa").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


def display(n, e, p, m):
    print(f"{n}\n{e}\n{p}\n{m}")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone, message)
        return render_template("contact.html",value=True)

    else:
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = MIMEMultipart()
    email_message['From'] = MY_EMAIL
    email_message['To'] = MY_EMAIL
    email_message['Subject'] = 'New Message'

    email_message.attach(MIMEText(f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}', 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, MY_EMAIL, email_message.as_string())
    except Exception as e:
        print("Error sending email:", e)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
