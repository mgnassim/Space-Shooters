from flask import redirect, session, url_for
from general_background.users import user_create, users_pull_file

user = user_create()
users = users_pull_file()


def logedin_check(language):
    if not int(session["user_id"]) >= 1:
        if language == 'NL':
            return redirect(url_for("login_backend_nl.login"))
        else:
            return redirect(url_for("login_backend_en.login"))
