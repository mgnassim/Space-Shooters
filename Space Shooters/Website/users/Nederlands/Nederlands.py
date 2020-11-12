import base64   #encriptie
import smtplib
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from flask import Blueprint, render_template, redirect, url_for, session, request, g

Nederlands = Blueprint("Nederlands", __name__, static_folder="static", template_folder="templates")

users = []

class User:
    def __init__(self, id, username, password, email, logins):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.logins = logins

    def __repr__(self):
        return f'<User: {self.username}>'

for line in open("../Website/accountfile.txt", "r").readlines():
    accounts = line.split()
    users.append(User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3], logins=accounts[4]))


@Nederlands.route("/Registration", methods=['GET', 'POST'])
def registration_nl():
    if request.method == "POST":

        totalusersnew = 1
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        email = request.form["email"]

        if password == password2:
            #encriptie
            message = password
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            password = base64_bytes.decode('ascii')

            for line in open("../Website/accountfile.txt", "r").readlines():
                totalusersnew += 1

            file = open("../Website/accountfile.txt", "a")
            file.write("\n")
            file.write(str(totalusersnew))
            file.write(" ")
            file.write(username)
            file.write(" ")
            file.write(password)
            file.write(" ")
            file.write(email)
            file.write(" ")
            file.write("0")
            file.close()

            users.append(User(id=totalusersnew, username=username, password=password, email=email, logins=accounts[4]))

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

                print("Email sent!")

            except:
                print("Something went wrong...")

            return redirect(url_for('Nederlands.login_nl'))

    return render_template("Space_Shooter_Web_NL_Registration.html")


@Nederlands.route('/login', methods=["GET", "POST"])
@Nederlands.route("/Login", methods=["GET", "POST"])
def login_nl():
    if request.method == 'POST':
        session.pop('user_id', None)
        line1 = 0

        username = request.form['username']
        password = request.form['password']

        try:
            user = [x for x in users if x.username == username][0]
        except:
            return redirect(url_for('Nederlands.login_nl'))
        else:
            base64_message = user.password
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            passwordencode = message_bytes.decode('ascii')

            if passwordencode == password:
                session['user_id'] = user.id
                if user.id == 1:
                    return redirect(url_for('Admin.admin'))
                else:
                    for line in open("../Website/accountfile.txt", "r").readlines():
                        accounts = line.split()
                        line1 += 1
                        if accounts[1] == user.username:
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
                            file.write(accounts[0] + " " + accounts[1] + " " + accounts[2] + " " + accounts[3] + " " + str(logins))
                            file.close()

                            users.append(
                                User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3],
                                     logins=logins))

                            return redirect(url_for('Nederlands.homepage_nl'))

            return redirect(url_for('Nederlands.login_nl'))

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
                            users.append(User(id=accounts[0], username=accounts[1], password=password, email=accounts[3], logins=accounts[4]))

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

    return render_template("Space_Shooter_Web_NL_Password_Reset.html")


@Nederlands.route("/RFID")
def RFID_nl():
    # Maakt een variable van de rfid
    reader = SimpleMFRC522()
    filecodes = []
    try:
        cardcode = reader.read()

        for line in open("../Website/highscore.txt", "r").readlines():
            filecodes.append(line)

        n = len(filecodes)

        for i in range(n):
            if cardcode[0] == filecodes[i]:
                return redirect(url_for('Nederlands.homepage_gast_nl'))
    finally:
        # Finally betekent dat het de code toch uitvoert
        # maakt niet uit of try/except false of true is.
        GPIO.cleanup()

    return render_template("Space_Shooter_Web_NL_RFID.html")

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
        array.append(scorebord[0] + " " + scorebord[1])

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


    return render_template("Space_Shooter_Web_NL_Homepage.html", list_to_send=array)

@Nederlands.route("/Homepage/Gast")
def homepage_gast_nl():
    return render_template("Space_Shooter_Web_NL_Homepage_Gast.html")