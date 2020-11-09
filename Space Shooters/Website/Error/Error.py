from flask import Blueprint, render_template, redirect, url_for, g

Error = Blueprint("Error", __name__, static_folder="static", template_folder="templates")


@Error.errorhandler(400)
def page_not_found(e):
    return render_template("400.html")

@Error.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
