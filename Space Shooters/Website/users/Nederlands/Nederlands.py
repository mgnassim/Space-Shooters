import base64       # encriptie protocol
import smtplib      # Email API
import datetime     # importeerd de momentele tijd

# Flask inport met de benodigde flask packages
from flask import Blueprint, render_template, redirect, url_for, session, request, g

# word de tijd geinitailseerd
now = datetime.datetime.now()
# Hier word aan gegeven dat dit bestand een flask blueprint is. met de naam Nederlands
Nederlands = Blueprint("Nederlands", __name__, static_folder="static", template_folder="templates")
# word Users array aangemaakt
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


# De weburl basis_url/NL/Regestration word hier aangemaakt. Met methods GET en Post om informatie van de HTML pagina te
# kunnen krijgen voor het Registeren.
# in dit stukje code word er een nieuw accout toe gevoegd aan het account database dat in het text bestand
# accoutfile.txt staat. Er word ook een E-mail verstuurd naar het ingevulde E-mail adres van het nieuw geregisteerde
# account.
@Nederlands.route("/Registration", methods=['GET', 'POST'])
def registration_nl():
    # word de file path aangegeven van accountfile.txt document wat later nodig is in het script.
    filename = "../Website/accountfile.txt"
    # Geeft aan dat de code gestard moet worden wanneer er op de html pagina een Post word gedaan met ingevulde
    # gebruikersnaam en wachtwoord.
    if request.method == "POST":
        # variable later nodig in het script wanneer er word geteld hoeveel accounts er al zijn voor de UserID
        totalusersnew = 1
        # hier worden de ingevulde gebruikersnaam, wachtwoord, conformatie wachtwoord en email opgevraagd
        # van de html pagina.
        # overgezet naar een python variable zodat het gebruikt kan worden in de rest van het scirpt.
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        email = request.form["email"]

        if password == password2:
            # base 64 encryptie met de encode ascii word uitgevoerd op het ingevulde wachtwoord voordat het word
            # opgeslagen zodat mensen niet gelijk het wachtwoord kunnen zien als ze toegang krijgen tot de wachtwoorden
            # dit word gedaan doormiddel van de base64 python package
            message = password
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            password = base64_bytes.decode('ascii')

            # accountfile.txt word regel voor regel gelezen en telt voor elke gelezen regen één user bij op zodat het
            # weet hoeveel accounts er zijn om een goed ID te geven aan het nieuwe accout dat gemaakt word.
            for line in open(filename, "r").readlines():
                totalusersnew += 1

            # accountfile.txt word geopend om er in te schrijven. wat er geschreven word is: totalusernem( UserID),
            # username, achtwoord, E-mailaddress, en de aantal logins dat er gedaan zijn wat nu nog 0 is want er is nog
            # niet ingelogt met dit account. Het bestand word hierna gesloten om geheugen te besparen,
            file = open(filename, "a")
            file.write("\n" + str(totalusersnew) + " " + username + " " + password + " " + email + " 0")
            file.close()

            # Er word een nieuwe gebruiker toe gevoegd aan de users array zoat het in het bestand kan worden opgevraagd
            # De array is opgeslagen in de RAM geheugen en het text document is voor het langdurige opslag.
            users.append(User(id=totalusersnew, username=username, password=password, email=email, logins=accounts[4]))

            # De email API om de registratie E-mail te versturen
            gmail_user = 'spaceshooters1@gmail.com'
            gmail_password = 'SpaceInvaders'

            sent_from = gmail_user
            to = email
            subject = 'SpaceShooters'
            body = 'Regestratie email van SpaceShooters'

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

            except:
                print("Something went wrong...")

            return redirect(url_for('Nederlands.login_nl'))

    # Hier word aangegeven welke HTML template gerender moet worden hier is dat Space_Shooter_Web_NL_Registration.html
    return render_template("Space_Shooter_Web_NL_Registration.html")


# De weburl basis_url/NL/login en basis_url/NL/Login word hier aangemaakt. de twee url hebben er mee te maken dat er 1
# met hoofdletter is en 1 zonder zodat er geen vergissing gemaakt kan worden en jer zoizo altijd de goede krijgt.
# Met methods GET en Post om informatie van de HTML pagina te kunnen krijgen voor het inloggen.
# Dit is de inlog pagina hier word de backend van het inloggen verhanddeld. De username en Wachtwoord dat je op de HTML
# pagina invult worden hier binnengekregen en word het vergeleken met de users array ofdat het er instaat.
# Wanneer het er instaat word het goedgekeurd en krijg je een session id en word je doorgestuurd naar de home pagina.
@Nederlands.route('/login', methods=["GET", "POST"])
@Nederlands.route("/Login", methods=["GET", "POST"])
def login_nl():
    # word de file path aangegeven van accountfile.txt document wat later nodig is in het script.
    filename = "../Website/accountfile.txt"
    # Geeft aan dat de code gestard moet worden wanneer er op de html pagina een Post word gedaan met ingevulde
    # gebruikersnaam en wachtwoord.
    if request.method == 'POST':
        # SessionID word gezet op 0. Er is geen SessionID
        session.pop('user_id', None)
        # Variable dat later word gebruikt bij het veraneren van het hoeveelheid aan logins in het accountfile.txt
        # document.
        line1 = 0
        # hier worden de ingevulde gebruikersnaam en wachtwoordopgevraagd van de html pagina.
        # Overgezet naar een python variable zodat het gebruikt kan worden in de rest van het scirpt.
        username = request.form['username']
        password = request.form['password']

        # Er word gekeken ofdat het ingevulde gebruikersnaam bestaad in het array users. Als het niet bestaand word je
        # weer terug gestuurd naar de login pagina.
        try:
            user = [x for x in users if x.username == username][0]
        except:
            return redirect(url_for('Nederlands.login_nl'))
        else:
            # base 64 Decryptie met de encode ascii word uitgevoerd op het opgeslagen wachtwoord. Zodat het vergeleken
            # kan worden met het ingevulde wachtwoord. Dit word gedaan doormiddel van de base64 python package
            base64_message = user.password
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            passwordencode = message_bytes.decode('ascii')

            # Hier word gekeken ofdat het ingevulde wachtwoord gelijk is met het wachtwoord gelijk is met het wachtwoord
            # dat geregisteerd staat met de ingeulde username.
            if passwordencode == password:
                # Hier krijgt de sessionID het id van de ingelogde user. Voor later gebruik bij ander pagina's.
                session['user_id'] = user.id
                # Hier word gekeken naar wat de userID is. Wanneer het 1 is betekkent dat er word ingelogd door de admin
                # account en word het doorgestuurd naar de admin pagina waar diagnostic van het apperaat uitgevoerd kan
                # worden.
                if int(user.id) == 1:
                    return redirect(url_for('Admin.admin'))
                else:
                    # accountfile.txt word regel voor regel gelezen. De gelezen regel word in het varriable line gezet.
                    for line in open(filename, "r").readlines():
                        # Het variable line word gesplitst op de spaties en word in het varariable accounts_login gezet
                        accounts_login = line.split()
                        # Hier word bijgehouden welke regel het bestand zit. Bij elke regel telt het er één bij op.
                        line1 += 1
                        if accounts_login[1] == user.username:
                            line_to_delete = line1
                            initial_line = 1
                            file_lines = {}

                            logins = int(accounts[4])
                            logins += 1

                            with open(filename) as f:
                                content = f.readlines()

                            for line in content:
                                file_lines[initial_line] = line.strip()
                                initial_line += 1

                            f = open(filename, "w")
                            for line_number, line_content in file_lines.items():
                                if line_number != line_to_delete:
                                    f.write('{}\n'.format(line_content))

                            f.close()
                            print('Deleted line: {}'.format(line_to_delete))

                            file = open(filename, "a")
                            file.write(
                                accounts[0] + " " + accounts[1] + " " + accounts[2] + " " + accounts[3] + " " +
                                    str(logins))
                            file.close()

                            users.append(
                                User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3],
                                     logins=logins))

                            return redirect(url_for('Nederlands.homepage_nl'))

            return redirect(url_for('Nederlands.login_nl'))

    # Hier word aangegeven welke HTML template gerender moet worden hier is dat Space_Shooter_Web_NL_Login.html
    return render_template("Space_Shooter_Web_NL_Login.html")


@Nederlands.route("/Password/Reset", methods=['GET', 'POST'])
def password_reset_nl():
    if request.method == "POST":
        username = request.form['username']
        email = request.form["email"]
        password = request.form['password']
        password2 = request.form['password2']

        if password == password2:
            try:
                user = [x for x in users if x.username == username][0]
            except:
                return redirect(url_for('Nederlands.registration_nl'))
            else:
                if user.email == email:
                    message = password
                    message_bytes = message.encode('ascii')
                    base64_bytes = base64.b64encode(message_bytes)
                    password = base64_bytes.decode('ascii')

                    line1 = 0

                    for line in open("../Website/accountfile.txtt", "r").readlines():
                        accounts = line.split()
                        line1 += 1
                        if accounts[1] == username & accounts[3] == email:
                            users.append(User(id=accounts[0], username=accounts[1], password=password,
                                              email=accounts[3], logins=accounts[4]))

                            filename = '../Website/accountfile.txt'
                            line_to_delete = line1
                            initial_line = 1
                            file_lines = {}

                            logins = int(accounts[4])
                            logins += 1

                            with open(filename) as f:
                                content = f.readlines()

                            for line in content:
                                file_lines[initial_line] = line.strip()
                                initial_line += 1

                            f = open(filename, "w")
                            for line_number, line_content in file_lines.items():
                                if line_number != line_to_delete:
                                    f.write('{}\n'.format(line_content))

                            f.close()
                            print('Deleted line: {}'.format(line_to_delete))

                            file = open(filename, "a")
                            file.write(
                                accounts[0] + " " + accounts[1] + " " + password + " " + accounts[3] + " " + accounts[4])

                    return redirect(url_for('Nederlands.login_nl'))

    # Hier word aangegeven welke HTML template gerender moet worden hier is dat Space_Shooter_Web_NL_Password_Reset.html
    return render_template("Space_Shooter_Web_NL_Password_Reset.html")


@Nederlands.route("/Homepage")
def homepage_nl():
    try:
        if not int(g.user.id) >= 1:
            return redirect(url_for('Nederlands.login_nl'))
    except:
        return redirect(url_for('Nederlands.login_nl'))

    array = []

    for line in open("../Website/highscore.txt", "r").readlines():
        scorebord = line.split()
        array.append(scorebord[1] + " " + scorebord[0])

    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    array.reverse()
    g.scourebord = array

    # Hier word aangegeven welke HTML template gerender moet worden hier is dat Space_Shooter_Web_NL_Homepage.html
    # De informatie van de array string word ook verstuurd naar de html pagina.
    return render_template("Space_Shooter_Web_NL_Homepage.html", list_to_send=array)