import base64
import smtplib

from flask import Blueprint, render_template, redirect, url_for, session, request, g

Nederlands = Blueprint("Nederlands", __name__, static_folder="static", template_folder="templates")

users = []

class User:
<<<<<<< .merge_file_a14496
    def __init__(self, id, username, password, email):
=======
    def __init__(self, id, username, password, email, logins):
>>>>>>> .merge_file_a01484
        self.id = id
        self.username = username
        self.password = password
        self.email = email
<<<<<<< .merge_file_a14496
=======
        self.logins = logins
>>>>>>> .merge_file_a01484

    def __repr__(self):
        return f'<User: {self.username}>'

for line in open("../Website/accountfile.txt", "r").readlines():
    accounts = line.split()
<<<<<<< .merge_file_a14496
    users.append(User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3]))
=======
    users.append(User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3], logins=accounts[4]))
>>>>>>> .merge_file_a01484

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

<<<<<<< .merge_file_a14496
            for line in open("../../accountfile.txt", "r").readlines():
                totalusersnew += 1

            file = open("../../accountfile.txt", "a")
=======
            for line in open("../Website/accountfile.txt", "r").readlines():
                totalusersnew += 1

            file = open("../Website/accountfile.txt", "a")
>>>>>>> .merge_file_a01484
            file.write("\n")
            file.write(str(totalusersnew))
            file.write(" ")
            file.write(username)
            file.write(" ")
            file.write(password)
            file.write(" ")
            file.write(email)
<<<<<<< .merge_file_a14496
            file.close()

            users.append(User(id=totalusersnew, username=username, password=password, email=email))
=======
            file.write(" ")
            file.write("0")
            file.close()

            users.append(User(id=totalusersnew, username=username, password=password, email=email, logins=accounts[4]))
>>>>>>> .merge_file_a01484

            gmail_user = 'spaceshooters1@gmail.com'
            gmail_password = 'SpaceInvaders'

            sent_from = gmail_user
            to = email
            subject = 'SpaceShooters'
            body = 'Regestratie email van SpaceShooters'

            email_text = """\
<<<<<<< .merge_file_a14496
            From: %s
            To: %s
            Subject: %s
    
            %s
            """ % (sent_from, ", ".join(to), subject, body)
=======
                    From: %s
                    To: %s
                    Subject: %s
            
                    %s
                    """ % (sent_from, ", ".join(to), subject, body)
>>>>>>> .merge_file_a01484

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()

                print("Email sent!")

            except:
                print("Something went wrong...")

<<<<<<< .merge_file_a14496

=======
>>>>>>> .merge_file_a01484
            return redirect(url_for('Nederlands.login_nl'))

    return render_template("Space_Shooter_Web_NL_Registration.html")


@Nederlands.route('/login', methods=["GET", "POST"])
@Nederlands.route("/Login", methods=["GET", "POST"])
def login_nl():
    if request.method == 'POST':
        session.pop('user_id', None)
<<<<<<< .merge_file_a14496
=======
        line1 = 0
>>>>>>> .merge_file_a01484

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
<<<<<<< .merge_file_a14496
                    return redirect(url_for('Nederlands.homepage_nl'))
=======
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

                            return redirect(url_for('Nederlands.homepage_nl'))
>>>>>>> .merge_file_a01484

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

<<<<<<< .merge_file_a14496
                for line in open("../../accountfile.txt", "r").readlines():
                    accounts = line.split()
                    if accounts[1] == username & accounts[3] == email:
                        users.append(User(id=accounts[0], username=accounts[1], password=password, email=accounts[3]))
=======
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
>>>>>>> .merge_file_a01484

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