from flask import Blueprint, render_template        # flask inport met de benodigde packages

# Blueprint word aangemaakt voor dit document.
error_detection = Blueprint("error_detection", __name__, static_folder="static", template_folder="templates")


# Als er een http error ontstaat word het hier ontvangen en komt er een custum error pagina te voorschijn op de site.
# Http error codes: https://nl.wikipedia.org/wiki/Lijst_van_HTTP-statuscodes
# Error 400: Foute aanvraag.
@error_detection.errorhandler(400)
def page_not_found(e):
    return render_template("400.html")


# Error 404: Webpagina niet gevonden.
@error_detection.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# Error 405: Methode niet toegestaan
@error_detection.errorhandler(405)
def page_not_found(e):
    return render_template("405.html")


# Error 409: Conflict
@error_detection.errorhandler(409)
def page_not_found(e):
    return render_template("409.html")
