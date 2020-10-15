from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Space_Shooter_Web_login_NL.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
