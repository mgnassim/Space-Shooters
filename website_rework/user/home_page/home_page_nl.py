from flask import render_template, Blueprint  # Flask inport met de benodigde flask packages
from user.home_page.home_page_scripts import logedin_check, bubble_sorting

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
home_page_nl = Blueprint("home_page_nl", __name__, static_folder="static", template_folder="templates")


@home_page_nl.route('/', methods=["GET", "POST"])
def home_page():
    language = 'NL'
    logedin_check(language)
    scoreboard_altime = bubble_sorting()
    return render_template("home_page_nl.html", list_to_send=scoreboard_altime)
