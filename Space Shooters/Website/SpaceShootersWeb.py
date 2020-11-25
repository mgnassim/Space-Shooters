# pip installed packages
import smtplib      # api module om email's te versturen
import socket       # ip achterhalen
from flask import Flask, render_template, redirect, session, g  # Flask inport met de benodigde flask packages

# eigen packages(Blueprint van flask)
from users.Nederlands.Nederlands import Nederlands
from users.Engels.Engels import Engels
from Admin.Admin import Admin
from Error.Error import Error
from Game.Game import Game

# users array aangemaakt
users = []


# word aan gegeven wat er in de array users komt te staan
class User:
    def __init__(self, id, username, password, email, logins):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.logins = logins

    def __repr__(self):
        return f'<User: {self.username}>'


# Het bestand met alle gebruikers word geopend en regel voor regel gelezen
# Na het lezen van de regel word het gesplitst en in de users array gezet waarna het later terug gevraagd kan worden.
for line in open("../Website/accountfile.txt", "r").readlines():
    accounts = line.split()
    users.append(User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3], logins=accounts[4]))


# Een script dat een Email stuurd naar Butrosgroot@gmail.com met het ipadres van het apperaat waar het op draait.
# Dat gebeurd bij het opstarten van het script. Het script gebruikt de Gmail API om e-mails te versturen.
def test():
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)

    # E-mail sturen
    gmail_user = 'spaceshooters1@gmail.com'
    gmail_password = 'SpaceInvaders'

    sent_from = gmail_user
    to = "butrosgroot@gmail.com"
    subject = 'SpaceShooters'
    body = ipaddr

    email_text = """\
            From: %s
            To: %s
            Subject: %s
            
            %s
            """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print("Email sent!")
    except:
        print("Something went wrong...")


# Flask word hier geimporteerd en in de variable app gezet
app = Flask(__name__)
# hier word een sercret key gemaakt zodat mensen niet zomaar de website op kunnen komen wanneer ze niet ingelogt zijn.
app.secret_key = 'somesecretkeythatonlyishouldknow'


# word uitgevoerd voordat je op de site komt
# ( het moment dat je op enter drukt en voordat je de webpagina te zien krijgt)
@app.before_request
def before_request():
    g.user = None

    # maakt een session id aan als gast
    if 'user_id' in session:
        try:
            user = [x for x in users if x.id == session['user_id']][0]
            g.user = user
        except:
            g.user = users[0]


# Is een redirect naar de login pagina wanneer je alleen de url van de website invult omdat er geen voor pagina is
# van de site. Dat normaal de plek heeft van de /
@app.route('/')
def link1():
    return redirect("/NL/Login")


# Wanneer er op een url word gezocht gaat het kijken naar welke bluepint( pythonpackage) het naar hoe word gestuurd.
# Alle zoek opdrachten worden door de Error detectie heen gehaald zodat wanneer er iets fout gaat dat het
# word opgevangen daar in. De nederlandse pagina's beginnen met /NL in de url dus die worden daar naartoe gestuurd
# enzovoort
app.register_blueprint(Error, url_prefix="")
app.register_blueprint(Nederlands, url_prefix="/NL")
app.register_blueprint(Engels, url_prefix="/EN")
app.register_blueprint(Admin, url_prefix="/admin")
app.register_blueprint(Game, url_prefix="/game")


# Hier word de talen temaplate gerenderd en mogelijk gemaakt dat er mensen naar toe kunnen gaan wanneer ze naar
# de webpagina basis_url/language toe gaan.
@app.route("/language")
def language_selection():
    return render_template("Space_Shooter_Web_Language_selector.html")


# Alles word gerund
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
