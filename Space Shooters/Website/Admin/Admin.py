from flask import Blueprint, render_template, redirect, url_for, g, request
import Adafruit_PCA9685  # Import library van PCA9685 module.
import RPi.GPIO as GPIO  # Import library GPIO


Admin = Blueprint("Admin", __name__, static_folder="static", template_folder="templates")

@Admin.route("/")
def admin():
    GPIO.setmode(GPIO.BCM)  # Aangeven welke type pin notering er gebruikt word
    GPIO.setwarnings(False)  # Zet waarschuwing uit

    sensor1 = 4
    sensor2 = 5
    sensor3 = 27
    sensor4 = 22
    sensor5 = 17

    # pinnen instellen
    GPIO.setup(sensor1, GPIO.IN)
    GPIO.setup(sensor2, GPIO.IN)
    GPIO.setup(sensor3, GPIO.IN)
    GPIO.setup(sensor4, GPIO.IN)
    GPIO.setup(sensor5, GPIO.IN)

    # puten
    geraakt = 0
    punten_nomering = 0

    pwm = Adafruit_PCA9685.PCA9685()  # Initialiseer de PCA9685 met het standaardadres (basis adddres 0x40).

    pwm.set_pwm_freq(50)  # Verander de PWM frequentrie naar 50MHZ

    # Hier congigureer ik de minimaale en maximaale waardes voor de pulse
    servo_actief = 100  # Min pulse length out of 4096
    servo_rust = 350  # Max pulse length out of 4096 (90 graden)
    servo1 = 15
    servo2 = 12
    servo3 = 0
    servo4 = 1
    servo5 = 7

    if request.method == "POST":
        Target = ["target"]

        if Target == 0:
            pwm.set_pwm(servo1, 0, servo_actief)
            while True:
                if GPIO.input(sensor1):
                    pwm.set_pwm(servo1, 0, servo_rust)
                    geraakt += 1
                    break


        if Target == 1:
            pwm.set_pwm(servo2, 0, servo_actief)
            while True:
                if GPIO.input(sensor2):
                    pwm.set_pwm(servo2, 0, servo_rust)
                    geraakt += 1
                    break


        if Target == 2:
            pwm.set_pwm(servo3, 0, servo_actief)
            while True:
                if GPIO.input(sensor3):
                    pwm.set_pwm(servo3, 0, servo_rust)
                    geraakt += 1
                    break


        if Target == 3:
            pwm.set_pwm(servo4, 0, servo_actief)
            while True:
                if GPIO.input(sensor4):
                    pwm.set_pwm(servo4, 0, servo_rust)
                    geraakt += 1
                    break


        if Target == 4:
            pwm.set_pwm(servo5, 0, servo_actief)
            while True:
                if GPIO.input(sensor5):
                    pwm.set_pwm(servo5, 0, servo_rust)
                    geraakt += 1
                    break

    return render_template("Space_Shooter_Web_Admin.html")