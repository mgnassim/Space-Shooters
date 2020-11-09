<<<<<<< .merge_file_a19700
from flask import Blueprint, render_template, redirect, url_for, g
=======
from flask import Blueprint, render_template
>>>>>>> .merge_file_a23176

Error = Blueprint("Error", __name__, static_folder="static", template_folder="templates")


@Error.errorhandler(400)
def page_not_found(e):
    return render_template("400.html")

<<<<<<< .merge_file_a19700
@Error.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
=======

@Error.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@Error.errorhandler(405)
def page_not_found(e):
    return render_template("405.html")


@Error.errorhandler(409)
def page_not_found(e):
    return render_template("409.html")
>>>>>>> .merge_file_a23176
