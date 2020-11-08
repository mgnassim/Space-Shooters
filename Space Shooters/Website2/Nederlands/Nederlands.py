import base64
import smtplib

from flask import Blueprint, render_template, redirect, url_for, session, request, g

Nederlands = Blueprint("Nederlands", __name__, static_folder="static", template_folder="templates")

users = []

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'<User: {self.username}>'

for line in open("C:/Users/butro/Desktop/Website2/accountfile.txt", "r").readlines():
    accounts = line.split()
    users.append(User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3]))

@Nederlands.route("/Registration", methods=['GET', 'POST'])
def registration_nl():
    if request.method == "POST":

        totalusersnew = 1
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        email = request.form["email"]

        if password == password2:
            message = password
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            password = base64_bytes.decode('ascii')

            for line in open("../accountfile.txt", "r").readlines():
                totalusersnew += 1

            file = open("../accountfile.txt", "a")
            file.write("\n")
            file.write(str(totalusersnew))
            file.write(" ")
            file.write(username)
            file.write(" ")
            file.write(password)
            file.write(" ")
            file.write(email)
            file.close()

            users.append(User(id=totalusersnew, username=username, password=password, email=email))

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
                return redirect(url_for('Nederlands.homepage_nl'))

            return redirect(url_for('Nederlands.login_nl'))

    return render_template("Space_Shooter_Web_NL_Login.html")


@Nederlands.route("/Password/Reset", methods=['GET', 'POST'])
def password_reset_nl():
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

                for line in open("../accountfile.txt", "r").readlines():
                    accounts = line.split()
                    if accounts[1] == username & accounts[3] == email:
                        users.append(User(id=accounts[0], username=accounts[1], password=password, email=accounts[3]))

                return redirect(url_for('Nederlands.login_nl'))

    return render_template("Space_Shooter_Web_NL_Password_Reset.html")


@Nederlands.route("/Homepage")
def homepage_nl():
    try:
        if not int(g.user.id) >= 1:
            return redirect(url_for('Nederlands.login_nl'))
    except:
        return redirect(url_for('Nederlands.login_nl'))

    return render_template("Space_Shooter_Web_NL_Homepage.html")