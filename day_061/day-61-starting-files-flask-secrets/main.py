from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms.validators import Email
from wtforms.validators import Length
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstraps = Bootstrap5(app)
app.secret_key = ""


@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstraps)


class MyForm(FlaskForm):
    Email = StringField(label='Email', validators=[Email()])
    Password = PasswordField(label='Password', validators=[Length(min=8)])
    Submit = SubmitField(label='Log In')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    email = login_form.Email.data
    password = login_form.Password.data
    print(email, password)
    if login_form.validate_on_submit():
        if login_form.Email.data == "admin@email.com" and login_form.Password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form, bootstrap=bootstraps)


if __name__ == '__main__':
    app.run(debug=True)
