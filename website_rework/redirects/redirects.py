from flask import Flask, render_template, redirect, session, g, Blueprint, url_for  # Flask inport met de benodigde flask packages

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
redirects = Blueprint("redirects", __name__, static_folder="static", template_folder="templates")


@redirects.route('/')
def login_redirect():
    return redirect(url_for("login_backend_nl.login"))
