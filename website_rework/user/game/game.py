from flask import render_template, Blueprint, url_for, redirect, request  # Flask inport met de benodigde flask packages
from user.game.game_script import game, game_deactiveate, game_activate, game_active_check

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
game_page = Blueprint("game_page", __name__, static_folder="static", template_folder="templates")


@game_page.route('/nl')
def game_site_nl():
    if request.method == "POST":
        print(game_active_check())
        game_activate()
        game()
        game_deactiveate()
        return redirect(url_for("home_page_nl.home_page"))
    return render_template("Space_Shooters_Web_game.html")


@game_page.route('/en')
def game_site_nl():
    if request.method == "POST":
        print(game_active_check())
        game_activate()
        game()
        game_deactiveate()
        return redirect(url_for("home_page_en.home_page"))
    return render_template("Space_Shooters_Web_game.html")

@game_page.route('/start')
def game_start():
    print(game_active_check())
    game_activate()
    game()
    game_deactiveate()
    return redirect(url_for("home_page_nl.home_page"))
