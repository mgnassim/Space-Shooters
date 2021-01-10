# Flask inport met de benodigde flask packages
from flask import Blueprint, session, g

# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
befor_request = Blueprint("befor_request", __name__,
                          static_folder="static", template_folder="templates")


# word uitgevoerd voordat je op de site komt
# ( het moment dat je op enter drukt en voordat je de webpagina te zien krijgt)
@befor_request.before_request
def before_request():
    g.user = None

    # maakt een session id aan als gast
    if 'user_id' in session:
        try:
            user = [x for x in g.users if x.id == session['user_id']][0]
            g.user = user
        except IndexError:
            g.user = g.users[0]
