from flask import Blueprint, render_template, redirect, url_for, g, request
import Adafruit_PCA9685  # Import library van PCA9685 module.
import RPi.GPIO as GPIO  # Import library GPIO
import time


Admin = Blueprint("Admin", __name__, static_folder="static", template_folder="templates")


def afstand_meting():
    GPIO.setmode(GPIO.BCM)  # Aangeven welke type pin notering er gebruikt word
    GPIO.setwarnings(False)  # Zet waarschuwing uit

    # afstandsensor
    TRIG = 23
    ECHO = 24
    GPIO.setup(TRIG, GPIO.OUT)  # Set pin als GPIO out
    GPIO.setup(ECHO, GPIO.IN)  # Set pin als GPIO in

    GPIO.output(TRIG, False)  # Set TRIG as LOW
    time.sleep(2)

    GPIO.output(TRIG, True)  # Verstuur een signaal(true)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)  # Zet trigger na 0,01ms naar 0(low)

    while GPIO.input(ECHO) == 0:  # Check als  de ECHO LOW (0) is
        pulse_start = time.time()  # Bewaar de genoteerde tijd van de low pulse

    while GPIO.input(ECHO) == 1:  # Check als  de ECHO HIGH (1) is
        pulse_end = time.time()  # Bewaar de laatst genoteerde tijd van de low pulse

    pulse_lengte = pulse_end - pulse_start  # bereken de pulse looptijd

    distance = (pulse_lengte * 24300) / 2  # vermenigvuldig met de sonische snelheid (34300 cm/s :2 ) omdat heen en weer
    distance = round(distance, 2)
    distance = int(distance)
    return distance


@Admin.route("/servo1")
def servo1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)

    sensor = 4
    GPIO.setup(sensor, GPIO.IN)

    servo_actief = 100
    servo_rust = 350
    servo = 11
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('Admin.admin'))


@Admin.route("/servo2")
def servo2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)

    sensor = 5
    GPIO.setup(sensor, GPIO.IN)

    servo_actief = 100
    servo_rust = 350
    servo = 12
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('Admin.admin'))


@Admin.route("/servo3")
def servo5():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)

    sensor = 17
    GPIO.setup(sensor, GPIO.IN)

    servo_actief = 100
    servo_rust = 350
    servo = 7
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('Admin.admin'))


@Admin.route("/servo4")
def servo4():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)

    sensor = 22
    GPIO.setup(sensor, GPIO.IN)

    servo_actief = 100
    servo_rust = 350
    servo = 1
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('Admin.admin'))


@Admin.route("/servo5")
def servo3():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)

    sensor = 27
    GPIO.setup(sensor, GPIO.IN)

    servo_actief = 100
    servo_rust = 350
    servo = 0
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('Admin.admin'))


@Admin.route("/", methods=['GET', 'POST'])
def admin():
    return render_template("Space_Shooter_Web_Admin.html")