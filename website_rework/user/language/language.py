# Flask inport met de benodigde flask packages
from flask import render_template, Blueprint

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
language = Blueprint("language", __name__,
                     static_folder="static", template_folder="templates")


@language.route('/', methods=["GET", "POST"])
def language_page():
    return render_template("language_selector_page.html")
