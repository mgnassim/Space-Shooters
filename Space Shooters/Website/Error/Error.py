from flask import Blueprint, render_template

Error = Blueprint("Error", __name__, static_folder="static", template_folder="templates")


@Error.errorhandler(400)
def page_not_found(e):
    return render_template("400.html")


@Error.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@Error.errorhandler(405)
def page_not_found(e):
    return render_template("405.html")


@Error.errorhandler(409)
def page_not_found(e):
    return render_template("409.html")
