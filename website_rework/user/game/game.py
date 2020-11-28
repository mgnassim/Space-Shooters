from flask import render_template, Blueprint  # Flask inport met de benodigde flask packages

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
game = Blueprint("game", __name__, static_folder="static", template_folder="templates")


@game.route('/', methods=["GET", "POST"])
def game_site_nl():
    return render_template("Space_Shooters_Web_game.html")
