from flask import Flask, render_template, redirect, url_for, session, request, g

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


users.append(User(id=0, username="admin", password="root", email="root@gmail.com"))
users.append(User(id=1, username="test", password="test", email="test@gmail.com"))

for line in open("accountfile.txt", "r").readlines():
    acounts = line.split()
    users.append(User(id=acounts[0], username=acounts[1], password=acounts[2], email=acounts[3]))
    totalusers += 1
    usernames += acounts[1]
    print(users)

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


@app.route('/')
def link():
    return redirect(url_for("login_nl"))


@app.route('/NL/login')
def link():
    return redirect(url_for("login_nl"))


@app.route('/nl/login')
def link():
    return redirect(url_for("login_nl"))


@app.route('/nl/Login')
def link():
    return redirect(url_for("login_nl"))


@app.route("/NL/Login", methods=["GET", "POST"])
def login_nl():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        print(users)

        try:
            user = [x for x in users if x.username == username][0]
        except:
            return redirect(url_for('login_nl'))
        else:
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('homepage_nl'))

    return render_template("Space_Shooter_Web_NL_Login.html")


@app.route('/EN/login')
def link():
    return redirect(url_for("login_en"))


@app.route('/en/login')
def link():
    return redirect(url_for("login_en"))


@app.route('/en/login')
def link():
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
            return redirect(url_for('login_nl'))
        else:
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('homepage_nl'))

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
        email = request.form["email"]

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

        return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_NL_Registration.html")


@app.route("/EN/Registration")
def registration_en():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

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

        return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_EN_Registration.html")


@app.route("/NL/Homepage")
def homepage_nl():
    if not g.user:
        return redirect(url_for('login_nl'))

    return render_template("Space_Shooter_Web_NL_Homepage.html")


@app.route("/EN/Homepage")
def homepage_en():
    return render_template("Space_Shooter_Web_EN_Homepage.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
