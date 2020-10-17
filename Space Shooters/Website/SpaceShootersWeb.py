from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def link():
    return redirect(url_for("login"))


@app.route('/login/')
def login():
    return render_template("Space_Shooter_Web_Login_NL.html")


@app.route('/language/')
def language():
    return render_template("Space_Shooter_Web_Login_NL.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
