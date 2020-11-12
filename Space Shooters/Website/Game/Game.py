# from __future__ import division                  #helpt bij het jet importen zorgt voor geen verwaring

import RPi.GPIO as GPIO  # Import library GPIO
import time, threading  # Import library Time.
import Adafruit_PCA9685  # Import library van PCA9685 module.
from random import randint
import smtplib

from flask import Blueprint, render_template, redirect, url_for, session, request, g

Game = Blueprint("Game", __name__, static_folder="static", template_folder="templates")

GPIO.setmode(GPIO.BCM)  # Aangeven welke type pin notering er gebruikt word
GPIO.setwarnings(False)  # Zet waarschuwing uit

# afstandsensor
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)  # Set pin als GPIO out
GPIO.setup(ECHO, GPIO.IN)  # Set pin als GPIO in

game_active = 0

def afstand_meting():
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


def game():
    # decaleer ik waarden
    sensor1 = 4
    sensor2 = 5
    sensor3 = 27

    # pinnen instellen
    GPIO.setup(sensor1, GPIO.IN)  # Pin 4 is input van sensor 3
    GPIO.setup(sensor2, GPIO.IN)  # Pin 27 is input van sensor 3
    GPIO.setup(sensor3, GPIO.IN)  # Pin 5 is input van sensor 3

    #puten
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
    servo5 = 5

    print('press Ctrl-C to quit...')

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_actief)  # draao90graden
    pwm.set_pwm(servo2, 0, servo_actief)  # draao90graden
    pwm.set_pwm(servo3, 0, servo_actief)  # draao90graden

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)

    time.sleep(1)

    tijd_limiet = 30  # aantal seconde dat er gespeeld kan worden
    start_tijd = time.time()  # start tijd is de actueele tijd van nu
    pervRandomTarget = -1
    while True:  # loop altijd
        gespeeld_tijd = time.time() - start_tijd  # berekening gespeelde tijd

        if gespeeld_tijd >= tijd_limiet:  # als gespeelde tijd groter is dan tijd limiet stop de loop
            break

        while True:
            RandomTarget = randint(0, 2)
            if RandomTarget != pervRandomTarget:
                break

        pervRandomTarget = RandomTarget

        if RandomTarget == 0:
            pwm.set_pwm(servo1, 0, servo_actief)
            while True:
                if GPIO.input(sensor1):
                    pwm.set_pwm(servo1, 0, servo_rust)
                    geraakt += 1
                    break

                if gespeeld_tijd > tijd_limiet:
                    break

        if RandomTarget == 1:
            pwm.set_pwm(servo2, 0, servo_actief)
            while True:
                if GPIO.input(sensor2):
                    pwm.set_pwm(servo2, 0, servo_rust)
                    geraakt += 1
                    break

                if gespeeld_tijd > tijd_limiet:
                    break

        if RandomTarget == 2:
            pwm.set_pwm(servo3, 0, servo_actief)
            while True:
                if GPIO.input(sensor3):
                    pwm.set_pwm(servo3, 0, servo_rust)
                    geraakt += 1
                    break

                if gespeeld_tijd > tijd_limiet:
                    break

    pwm.set_pwm(servo1, 0, servo_actief)
    pwm.set_pwm(servo2, 0, servo_actief)
    pwm.set_pwm(servo3, 0, servo_actief)

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)
    print('game over')

    afstand = afstand_meting()

    if afstand < 10:
        punten_nomering = 0

    elif afstand >= 10 & afstand <= 30:
        punten_nomering = 1

    elif afstand >= 30 & afstand < 50:
        punten_nomering = 2

    elif afstand >= 50 & afstand <= 100:
        punten_nomering = 3

    elif afstand > 100:
        punten_nomering = 4

    totaalscore = geraakt * punten_nomering
    print(totaalscore)
    print(afstand)
    print('targets geraakt ' + str(geraakt) + ' score is ' + str(totaalscore) + ' nomering ' + str(punten_nomering))
    print(totaalscore)

@Game.route("/", methods=['GET', 'POST'])
def game_site_nl(game_active=game_active):
    if game_active == 0:
        game_active = 1
        game()
        game_active = 0
        return redirect(url_for('Nederlands.homepage_nl'))
    else:
        return redirect(url_for('Nederlands.homepage_nl'))

    return render_template("Space_Shooters_Web_game.html")
