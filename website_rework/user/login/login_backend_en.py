from flask import render_template, Blueprint, request  # Flask inport met de benodigde flask packages
from user.login.login_scripts import login_script, registration_script, password_reset_script

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
login_backend_en = Blueprint("login_backend_en", __name__, static_folder="static", template_folder="templates")


@login_backend_en.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return login_script()
    return render_template("Login_page_en.html")


@login_backend_en.route('/registration', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        return registration_script()
    return render_template("registration_page_en.html")


@login_backend_en.route('/reset', methods=["GET", "POST"])
def password_reset():
    if request.method == "POST":
        return password_reset_script()
    return render_template("password_reset_page_en.html")
