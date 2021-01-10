# Flask inport met de benodigde flask packages
from flask import render_template, Blueprint, request
from user.login.login_scripts import login_script, registration_script, password_reset_script

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
login_backend_nl = Blueprint(
    "login_backend_nl", __name__, static_folder="static", template_folder="templates")


@login_backend_nl.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        language = 'NL'
        return login_script(language)
    return render_template("Login_page_nl.html")


@login_backend_nl.route('/registration', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        language = 'NL'
        return registration_script(language)
    return render_template("registration_page_nl.html")


@login_backend_nl.route('/reset', methods=["GET", "POST"])
def password_reset():
    if request.method == "POST":
        language = 'NL'
        return password_reset_script(language)
    return render_template("password_reset_page_nl.html")
