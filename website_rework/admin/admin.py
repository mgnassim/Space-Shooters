from flask import render_template, Blueprint
from admin.admin_scripts import servo1_test, servo2_test, servo3_test, servo4_test, servo5_test

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")


@admin.route("/", methods=['GET', 'POST'])
def admin_web():
    return render_template("Space_Shooter_Web_Admin.html")


@admin.route("/servo1")
def servo_1():
    return servo1_test()


@admin.route("/servo2")
def servo_2():
    return servo2_test()


@admin.route("/servo3")
def servo_3():
    return servo3_test()


@admin.route("/servo4")
def servo_4():
    return servo4_test()


@admin.route("/servo5")
def servo_5():
    return servo5_test()
