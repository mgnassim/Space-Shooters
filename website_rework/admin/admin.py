from flask import Blueprint, render_template
from admin.admin_scripts import servo1_test, servo2_test, servo3_test, servo4_test, servo5_test

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")


@admin.route("/", methods=['GET', 'POST'])
def admin():
    return render_template("Space_Shooter_Web_Admin.html")


@admin.route("/servo1")
def servo1():
    return servo1_test()


@admin.route("/servo2")
def servo2():
    return servo2_test()


@admin.route("/servo3")
def servo3():
    return servo3_test()


@admin.route("/servo4")
def servo4():
    return servo4_test()


@admin.route("/servo5")
def servo5():
    return servo5_test()
