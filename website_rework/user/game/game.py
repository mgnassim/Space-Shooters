from flask import render_template, Blueprint, url_for, redirect, request  # Flask inport met de benodigde flask packages
# from user.game.game_script import game, game_deactiveate, game_activate, game_active_check
from database.database import nieuwste_score

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
game_page = Blueprint("game_page", __name__, static_folder="static", template_folder="templates")


# @game_page.route('/nl')
# def game_site_nl():
#     return render_template("Space_Shooters_Web_game.html")


# @game_page.route('/en')
# def game_site_en():
#     return render_template("Space_Shooters_Web_game.html")


# @game_page.route('/start')
# def game_start():
#     print(game_active_check())
#     game_activate()
#     game()
#     game_deactiveate()
#     return redirect(url_for("game_page.scoreboard"))


@game_page.route('/score')
def scoreboard():
    score = nieuwste_score()
    
    print(score[1])
    Gemiddelde_tijd = int(score[1])/30
    return render_template("Scoreboard_nl.html", totaalscore=str(score[0]), geraakt=str(score[1]), 
        afstand_speler=str(score[2]), Geraakte_targets=str(score[3]), Gemiddelde_tijd=str(round(
            Gemiddelde_tijd, 2)))
