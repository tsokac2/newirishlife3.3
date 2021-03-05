import os
from flask import Flask, request, session
from flask_wtf import FlaskForm
from wtforms import(
    StringField, PasswordField, SubmitField,
    TextAreaField, SelectField)
from wtforms.validators import (
    DataRequired, Length, Regexp,
    Email, EqualTo, ValidationError)
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


class RegisterForm(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired("Enter your username!"), Length(
            min=2, message="Must be at least more than 1 character"),
            Length(max=15, message="Max 15 characters!"), Regexp(
                "^\w+$", message="Only letters numbers or underscore")],
        render_kw={"placeholder": "Username"})

    email = StringField("email", validators=[DataRequired("Enter your email"),
                        Email("An email address must contain a single @")],
                        render_kw={"placeholder": "Email"})

    password = PasswordField(
        "password", [DataRequired("Enter a password"), Length(
            min=6, message="Password must be at least 6 character")],
        render_kw={"placeholder": "Password"})

    confirm_password = PasswordField(
        "Confirm Password", [DataRequired("Confirm password"), EqualTo(
            "password", "Passwords must match")],
        render_kw={"placeholder": "Confirm Password"})

    submit = SubmitField("SIGN UP")

    def validate_username(self, username):
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user:
            raise ValidationError("Username is taken, choose a different one")

    def validate_email(self, email):
        email = mongo.db.users.find_one({"email": request.form.get("email")})
        if email:
            raise ValidationError("Email is taken, choose a different one!")


class LoginForm(FlaskForm):

    username = StringField(
        "username", validators=[DataRequired(
            "Enter your username")],
        render_kw={"placeholder": "Your username"})

    password = PasswordField(
        "password", validators=[DataRequired(
            "Enter correct password!")],
        render_kw={"placeholder": "Your password"})

    submit = SubmitField("LOGIN")


class AddTip(FlaskForm):
    tip_title = StringField(
        "tip_title", validators=[DataRequired("Enter a tip title"), Length(
            min=5, message="Must be more that 5 character!"), Length(
                max=50, message="Max length 50 characters!")],
        render_kw={"placeholder": "Tip Title"})

    tip_description = TextAreaField(
        "tip_description", validators=[DataRequired(
            "Enter a tip description"), Length(
                min=10, message="Must be more that 10 characters!"), Length(
                    max=500, message="Max length 300 characters!")],
        render_kw={"placeholder": "Tip Description"})

    submit = SubmitField("POST")
