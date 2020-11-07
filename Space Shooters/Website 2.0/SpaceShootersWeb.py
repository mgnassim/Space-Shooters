from flask import Flask, render_template, redirect, url_for, session, request, g
import base64
import smtplib
import socket

acounts = []
users = []
totalusers = 1
usernames = []


class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'<User: {self.username}>'


for line in open("accountfile.txt", "r").readlines():
    accounts = line.split()
    users.append(User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3]))
    totalusers += 1
    usernames += accounts[1]

##by start send email of connected ip
##enable this when deployd
def multiline_example():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    gmail_user = 'spaceshooters1@gmail.com'
    gmail_password = 'SpaceInvaders'

    sent_from = gmail_user
    to = "butrosgroot@gmail.com"
    subject = 'SpaceShooters'
    body = IPAddr

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


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/')
def link1():
    return redirect(url_for("login_nl"))


@app.route('/NL/login')
def link2():
    return redirect(url_for("login_nl"))


@app.route('/nl/login')
def link3():
    return redirect(url_for("login_nl"))


@app.route('/nl/Login')
def link4():
    return redirect(url_for("login_nl"))


@app.route("/NL/Login", methods=["GET", "POST"])
def login_nl():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        try:
            user = [x for x in users if x.username == username][0]
        except:
            return redirect(url_for('login_nl'))
        else:
            base64_message = user.password
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            passwordencode = message_bytes.decode('ascii')

            if passwordencode == password:
                session['user_id'] = user.id
                if user.id == 1:
                    return redirect(url_for('admin'))
                return redirect(url_for('homepage_nl'))

            return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_NL_Login.html")


@app.route('/EN/login')
def link5():
    return redirect(url_for("login_en"))


@app.route('/en/login')
def link6():
    return redirect(url_for("login_en"))


@app.route('/en/login')
def link7():
    return redirect(url_for("login_en"))


@app.route("/EN/Login", methods=['GET', 'POST'])
def login_en():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        try:
            user = [x for x in users if x.username == username][0]
        except:
            return redirect(url_for('login_en'))
        else:
            base64_message = user.password
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            passwordencode = message_bytes.decode('ascii')

            print(passwordencode)

            if passwordencode == password:
                session['user_id'] = user.id
                if user.id == 0:
                    return redirect(url_for('admin'))
                return redirect(url_for('homepage_en'))

            return redirect(url_for('login_en'))

    return render_template("Space_Shooter_Web_EN_Login.html")


@app.route("/language")
def language_selection():
    return render_template("Space_Shooter_Web_Language-Selection.html")


@app.route("/NL/Registration", methods=['GET', 'POST'])
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

            for line in open("accountfile.txt", "r").readlines():
                totalusersnew += 1

            file = open("accountfile.txt", "a")
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


            return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_NL_Registration.html")


@app.route("/EN/Registration", methods=['GET', 'POST'])
def registration_en():
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

            for line in open("accountfile.txt", "r").readlines():
                totalusersnew += 1

            file = open("accountfile.txt", "a")
            file.write("\n")
            file.write(str(totalusers))
            file.write(" ")
            file.write(username)
            file.write(" ")
            file.write(password)
            file.write(" ")
            file.write(email)
            file.close()

            users.append(User(id=totalusers, username=username, password=password, email=email))

            gmail_user = 'spaceshooters1@gmail.com'
            gmail_password = 'SpaceInvaders'

            sent_from = gmail_user
            to = email
            subject = 'SpaceShooters'
            body = 'registration email'

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

                print('Email sent!')
            except:
                print('Something went wrong...')

            return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_EN_Registration.html")


@app.route("/NL/Homepage")
def homepage_nl():
    try:
        if not int(g.user.id) >= 1:
            return redirect(url_for('login_nl'))
    except:
        return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_NL_Homepage.html")


@app.route("/EN/Homepage")
def homepage_en():
    try:
        if not int(g.user.id) >= 1:
            return redirect(url_for('login_EN'))
    except:
        return redirect(url_for('login_EN'))

    return render_template("Space_Shooter_Web_EN_Homepage.html")


@app.route("/Admin")
def admin():
    if not g.user.id == 0:
        return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_Admin.html")


@app.route("/NL/Password/Reset", methods=['GET', 'POST'])
def password_reset_nl():
    username = request.form['username']
    email = request.form["email"]
    password = request.form['password']
    password2 = request.form['password']

    if password == password2:
        try:
            user = [x for x in users if x.username == username][0]
        except:
            return redirect(url_for('password_reset_nl'))
        else:
            if user.email == email:
                message = password
                message_bytes = message.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                password = base64_bytes.decode('ascii')

                for line in open("accountfile.txt", "r").readlines():
                    accounts = line.split()
                    if accounts[1] == username & accounts[3] == email:
                        users.append(User(id=accounts[0], username=accounts[1], password=password, email=accounts[3]))

                return redirect(url_for('login_nl'))


    return render_template("Space_Shooter_Web_Password_Request.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
