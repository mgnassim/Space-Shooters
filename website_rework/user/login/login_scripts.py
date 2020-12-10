import base64
import os

from flask import redirect, session, request, url_for
from general_background.users import users_pull_file
from database.database import username_list_add, password_update, username_list_create

user = username_list_create()
users = users_pull_file()
account_file = "../website_rework/text_files/accounts.txt"
active_user_file = "../website_rework/text_files/active_user.txt"


def login_script():
    global account_file
    global users
    session.pop("user_id", None)
    username = request.form["username"]
    password = request.form["password"]

    try:
        user_login = [x for x in users if x.username == username][0]
    except IndexError:
        return redirect(url_for("login_backend_nl.login"))

    base64_message = user_login.password
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    passwordencode = message_bytes.decode('ascii')

    if passwordencode == password:
        with open(active_user_file, "r") as f:
            lines = f.readlines()
            f.close()

        with open(active_user_file, "w") as f:
            for line in lines:
                line.strip("\n")
            f.write(user_login.username)
            f.close()

        session["user_id"] = user_login.id
        with open(account_file, "r") as f:
            lines = f.readlines()
            f.close()

        with open(account_file, "w") as f:
            for line in lines:
                if line.strip("\n") != (
                    user_login.id + " " + user_login.username + " " + user_login.password + " " + user_login.email + " "
                        + (str(user_login.logins))):
                    f.write(line)

            user_login.logins += 1
            f.write(user_login.id + " " + user_login.username + " " + user_login.password + " " + user_login.email + " " +
                    str(user_login.logins))
            f.close()
        if user_login.id == 1:
            return redirect(url_for("admin.admin"))
        return redirect(url_for("home_page_nl.home_page"))


def registration_script():
    global account_file
    global users
    global user
    number_of_users = (len(users) + 1)  # array tellen begint bij 0 en heb nodig dat het bij 1 start

    username = request.form["username"]
    wachtwoord = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    if wachtwoord == password2:
        message = wachtwoord
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        wachtwoord = base64_bytes.decode('ascii')

        username_list_add(number_of_users, username, wachtwoord, email)

        return redirect(url_for("login_backend_nl.login"))

    return redirect(url_for("login_backend_nl.registration"))


def password_reset_script():
    global account_file
    global users

    username = request.form["username"]
    wachtwoord = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    try:
        user_login = [x for x in users if x.username == username][0]
    except IndexError:
        return redirect(url_for('Nederlands.registration_nl'))
    if wachtwoord == password2 and email == user.email:
        message = wachtwoord
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        password = base64_bytes.decode('ascii')

        password_update(wachtwoord, user_login)

        user_login.password = password

        return redirect(url_for("login_backend_nl.login"))

    return redirect(url_for("login_backend_nl.password_reset"))
