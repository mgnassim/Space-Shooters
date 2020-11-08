from flask import Blueprint, render_template, redirect, url_for, g

Admin = Blueprint("Admin", __name__, static_folder="static", template_folder="templates")

@Admin.route("/")
def admin():
    return render_template("Space_Shooter_Web_Admin.html")