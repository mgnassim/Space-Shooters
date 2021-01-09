from flask import render_template, Blueprint

# from admin.admin_scripts import servo1_test, servo2_test, servo3_test, servo4_test, servo5_test
from database.database import aantal_logins, aantal_games, rfid_codes_add
#from rfid.rfid_scripts import rfid_scan

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")


@admin.route("/", methods=["GET", "POST"])
def admin_web():
    return render_template("Admin_page.html", login_board=aantal_logins(), aantal_games_board=aantal_games())


#@admin.route("/rfid", methods=["GET", "POST"])
#def admin_web():
#    rfid_code = rfid_scan()
#    rfid_codes_add(rfid_code)



#@admin.route("/servo1")
#def servo_1():
#    return servo1_test()


#@admin.route("/servo2")
#def servo_2():
#    return servo2_test()


#@admin.route("/servo3")
#def servo_3():
#    return servo3_test()


#@admin.route("/servo4")
#def servo_4():
#    return servo4_test()


#@admin.route("/servo5")
#def servo_5():
#    return servo5_test()
