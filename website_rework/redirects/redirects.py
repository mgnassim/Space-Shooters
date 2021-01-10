# Flask inport met de benodigde flask packages
from flask import redirect, Blueprint, url_for

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
redirects = Blueprint("redirects", __name__,
                      static_folder="static", template_folder="templates")


@redirects.route('/')
def login_redirect():
    return redirect(url_for("login_backend_nl.login"))
