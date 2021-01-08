from flask import render_template, Blueprint  # Flask inport met de benodigde flask packages
from user.home_page.home_page_scripts import logedin_check
from database.database import score_list, score_list_personal

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
home_page_en = Blueprint("home_page_en", __name__, static_folder="static", template_folder="templates")


@home_page_en.route('/', methods=["GET", "POST"])
def home_page():
    language = 'EN'
    logedin_check(language)
    return render_template("home_page_en.html", general_scoreboard=score_list(), personal_scoreboard=score_list_personal())
