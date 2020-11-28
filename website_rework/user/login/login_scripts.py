import base64

from flask import redirect, session, request, url_for
from general_background.users import user_create, users_pull_file

user = user_create()
users = users_pull_file()


def login_script():
    account_file = (
        "C:/Users/butro/Desktop/Google drive/Projecten/Code/Python/PycharmProjects/Home_Control/text_files/accounts.txt"
    )
    global users
    session.pop("user_id", None)
    username = request.form["username"]
    password = request.form["password"]

    try:
        user_login = [x for x in users if x.username == username][0]
    except IndexError:
        return redirect(url_for("login_backend.login"))

    base64_message = user.password
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    passwordencode = message_bytes.decode('ascii')

    if passwordencode == password:
        session["user_id"] = user_login.id
        with open(account_file, "r") as f:
            lines = f.readlines()

        with open(account_file, "w") as f:
            for line in lines:
                if line.strip("\n") != (
                    user_login.id + " " + user_login.username + " " + user_login.password + " " + user_login.email + " "
                        + (str(user_login.logins))):
                    f.write(line)

            user_login.logins += 1
            f.write(user.id + " " + user_login.username + " " + user_login.password + " " + user_login.email + " " +
                    str(user_login.logins))
            f.close()

        return redirect(url_for("home.home_page"))


def registration_script():
    account_file = (
        "C:/Users/butro/Desktop/Google drive/Projecten/Code/Python/PycharmProjects/Home_Control/text_files/accounts.txt"
    )
    global users
    global user
    number_of_users = (len(users) + 1)  # array tellen begint bij 0 en heb nodig dat het bij 1 start

    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    if password == password2:
        message = password
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        password = base64_bytes.decode('ascii')

        file = open(account_file, "a")
        file.write("\n" + str(number_of_users) + " " + username + " " + password + " " + email + " 0")
        file.close()

        users.append(user(id=number_of_users, username=username, password=password, email=email, logins="0"))

        return redirect(url_for("login_backend.login"))

    return redirect(url_for("login_backend.registration"))


def password_reset_script():
    account_file = (
        "C:/Users/butro/Desktop/Google drive/Projecten/Code/Python/PycharmProjects/Home_Control/text_files/accounts.txt"
    )
    global users

    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    try:
        user_login = [x for x in users if x.username == username][0]
    except IndexError:
        return redirect(url_for('Nederlands.registration_nl'))
    if password == password2 and email == user.email:
        message = password
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        password = base64_bytes.decode('ascii')

        user_login.password = password

        session["user_id"] = user.id
        with open(account_file, "r") as f:
            lines = f.readlines()

        with open(account_file, "w") as f:
            for line in lines:
                if line.strip("\n") != (
                        user_login.id + " " + user_login.username + " " + user_login.password + " " + user_login.email +
                        " " + (str(user_login.logins))):
                    f.write(line)

            f.write(user.id + " " + user_login.username + " " + user_login.password + " " + user_login.email + " " +
                    str(user_login.logins))
            f.close()

        return redirect(url_for("login_backend.login"))

    return redirect(url_for("login_backend.password_reset"))
