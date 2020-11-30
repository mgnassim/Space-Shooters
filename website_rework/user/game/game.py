from flask import render_template, Blueprint, url_for  # Flask inport met de benodigde flask packages
from user.game.game_script import game, game_deactiveate, game_activate, game_active_check

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
game_page = Blueprint("game_page", __name__, static_folder="static", template_folder="templates")


@game_page.route('/', methods=["GET", "POST"])
def game_site_nl():
    web_start = False
    while True:
        if web_start:
            if game_active_check() == 0:
                game_activate()
                game()
                game_deactiveate()
                return url_for("home_page_nl.home")
        web_start = True
        return render_template("Space_Shooters_Web_game.html")
