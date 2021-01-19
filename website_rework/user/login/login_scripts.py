import base64
import os

from flask import redirect, session, request, url_for
from general_background.users import users_pull_file, user_create
from database.database import username_list_add, password_update, username_list_create, username_list_create, logins_update

user = user_create()
users = username_list_create()


def login_script(language):
    global users
    global user
    session.pop("user_id", None)
    username = request.form["username"]
    password = request.form["password"]

    try:
        user_login = [x for x in users if x.username.lower() == username.lower()][0]
    except IndexError:
        if language == 'NL':
            return redirect(url_for("login_backend_nl.login"))
        else:
            return redirect(url_for("login_backend_en.login"))

    base64_message = user_login.password
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    passwordencode = message_bytes.decode('ascii')

    try:
        if passwordencode == password:
            logins_update(user_login)

            session["user_id"] = user_login.id

            users.pop()
            users = username_list_create()

            if int(user_login.id) == 1:
                return redirect(url_for("admin.admin_web"))

            if language == 'NL':
                return redirect(url_for("home_page_nl.home_page"))
            else:
                return redirect(url_for("home_page_en.home_page"))

    except:
        if language == 'NL':
            return redirect(url_for("login_backend_nl.login"))
        else:
            return redirect(url_for("login_backend_en.login"))
        
    


def registration_script(language):
    global account_file
    global users
    global user
    # array tellen begint bij 0 en heb nodig dat het bij 1 start
    number_of_users = (len(users) + 1)

    username = request.form["username"]
    wachtwoord = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    if wachtwoord == password2:
        message = wachtwoord
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        wachtwoord = base64_bytes.decode('ascii')

        username_list_add(number_of_users, username.lower(), wachtwoord, email)

        users.append(user(id=number_of_users, username=username,
                          password=wachtwoord, email=email, logins=0))

        if language == 'NL':
            return redirect(url_for("login_backend_nl.login"))
        else:
            return redirect(url_for("login_backend_en.login"))

    if language == 'NL':
        return redirect(url_for("login_backend_nl.registration"))
    else:
        return redirect(url_for("login_backend_en.registration"))


def password_reset_script(language):
    global account_file
    global users

    username = request.form["username"]
    wachtwoord = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    try:
        user_login = [x for x in users if x.username.lower() == username.lower()][0]
    except IndexError:
        if language == 'NL':
            return redirect(url_for('login_backend_nl.password_reset'))
        else:
            return redirect(url_for('login_backend_nl.password_reset'))

    if wachtwoord == password2 and email.lower() == user_login.email.lower():
        message = wachtwoord
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        password = base64_bytes.decode('ascii')

        password_update(password, user_login)

        users.pop()
        users = username_list_create()

        if language == 'NL':
            return redirect(url_for("login_backend_nl.login"))
        else:
            return redirect(url_for("login_backend_en.login"))

    if language == 'NL':
        return redirect(url_for("login_backend_nl.password_reset"))
    else:
        return redirect(url_for("login_backend_en.password_reset"))
