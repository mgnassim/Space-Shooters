from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def link():
    return redirect(url_for("home_nl"))


@app.route("/NL/RFID")
def rfid_nl():
    return render_template("Space_Shooter_Web_RFID_NL.html")


@app.route("/EN/RFID")
def rfid_en():
    return render_template("Space_Shooter_Web_RFID_EN.html")


@app.route("/language/")
def language():
    return render_template("Space_Shooter_Web_language_selector.html")


@app.route("/EN/login")
def login_en():
    return render_template("Space_Shooter_Web_Login_EN.html")


@app.route("/EN/register")
def register_en():
    return render_template("Space_Shooter_Web_register_EN.html")


@app.route("/NL/home")
def home_nl():
    return render_template("Space_Shooter_Web_NL_Homepage.html")


@app.route("/EN/home")
def home_en():
    return render_template("Space_Shooter_Web_Home_Page_EN.html")


@app.route("/NL/home")
def home2_nl():
    return render_template("Space_Shooter_Web_NL_Homepage.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
