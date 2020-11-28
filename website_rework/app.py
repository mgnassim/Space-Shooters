from flask import Flask

from general_background.befor_request import befor_request
from redirects.redirects import redirects
from user.login.login_backend_nl import login_backend_nl
from user.login.login_backend_en import login_backend_en
from user.home_page.home_page_nl import home_page_nl
from user.home_page.home_page_en import home_page_en
from user.language.language import language
from user.game.game import game
from error_detection.error_detection import error_detection

app = Flask(__name__)
app.secret_key = "8lxYKK24Tghvolv9ElokdxGj9fnCT7tZ"

app.register_blueprint(befor_request, url_prefix="")
app.register_blueprint(redirects, url_prefix="")
app.register_blueprint(login_backend_nl, url_prefix="/nl")
app.register_blueprint(login_backend_en, url_prefix="/en")
app.register_blueprint(home_page_nl, url_prefix="/nl/home")
app.register_blueprint(home_page_en, url_prefix="/en/home")
app.register_blueprint(language, url_prefix="/language")
app.register_blueprint(game, url_prefix="/game")
app.register_blueprint(error_detection, url_prefix="")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
