from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def link():
    return redirect(url_for("login_nl"))


@app.route("/NL/login")
def login_nl():
    return render_template("Space_Shooter_Web_Login_NL.html")


@app.route("/EN/login")
def login_en():
    return render_template("Space_Shooter_Web_Login_EN.html")


@app.route("/language/")
def language():
    return render_template("Space_Shooter_Web_language_selector.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
