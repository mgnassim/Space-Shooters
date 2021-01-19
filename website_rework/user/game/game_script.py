import RPi.GPIO as GPIO  # Import library GPIO
import time  # Import library Time.
import Adafruit_PCA9685  # Import library van PCA9685 module.
from random import randint
import datetime

from flask import Blueprint, session
from database.database import score_list_add

account_file = "../website_rework/text_files/accounts.txt"

game_active = "../website_rework/text_files/game_active.txt"

highscore = "../website_rework/text_files/highscore.txt"

active_user_file = "../website_rework/text_files/active_user.txt"

now = datetime.datetime.now()

Game = Blueprint("Game", __name__, static_folder="static",
                 template_folder="templates")

GPIO.setmode(GPIO.BCM)  # Aangeven welke type pin notering er gebruikt word
GPIO.setwarnings(False)  # Zet waarschuwing uit

# afstandsensor
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)  # Set pin als GPIO out
GPIO.setup(ECHO, GPIO.IN)  # Set pin als GPIO in

game_active = 0

# game gpio pinnen worden aan gegeven en gearmd
# decaleer ik waarden
sensor1 = 4
sensor2 = 5
sensor3 = 27
sensor4 = 22
sensor5 = 17

# Hier congigureer ik de minimaale en maximaale waardes voor de pulse
servo_actief = 100  # Min pulse length out of 4096
servo_rust = 350  # Max pulse length out of 4096 (90 graden)
servo1 = 15
servo2 = 12
servo3 = 0
servo4 = 1
servo5 = 7

# pinnen instellen
GPIO.setup(sensor1, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)
GPIO.setup(sensor3, GPIO.IN)
GPIO.setup(sensor4, GPIO.IN)
GPIO.setup(sensor5, GPIO.IN)

# Initialiseer de PCA9685 met het standaardadres (basis adddres 0x40).
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)  # Verander de PWM frequentrie naar 50MHZ

perv_random_target = -1
punten_nomering = 0
afstand = 0


def afstand_meting():
    GPIO.output(TRIG, False)  # Set TRIG as LOW
    time.sleep(0.5)

    GPIO.output(TRIG, True)  # Verstuur een signaal(true)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)  # Zet trigger na 0,01ms naar 0(low)

    while GPIO.input(ECHO) == 0:  # Check als  de ECHO LOW (0) is
        pulse_start = time.time()  # Bewaar de genoteerde tijd van de low pulse

    while GPIO.input(ECHO) == 1:  # Check als  de ECHO HIGH (1) is
        pulse_end = time.time()  # Bewaar de laatst genoteerde tijd van de low pulse

    pulse_lengte = pulse_end - pulse_start  # bereken de pulse looptijd

    # vermenigvuldig met de sonische snelheid (34300 cm/s :2 ) omdat heen en weer
    distance = (pulse_lengte * 34300) / 2
    distance = round(distance, 2)
    distance = int(distance)
    return distance


def punten_nomering_cal(afstand):
    if int(afstand) < 30:
        punten_nomering = 1
        return punten_nomering

    elif 50 >= int(afstand) > 100:
        punten_nomering = 2
        return punten_nomering

    elif 100 >= int(afstand) > 150:
        punten_nomering = 3
        return punten_nomering

    else:
        punten_nomering = 4
        return punten_nomering


def all_servos_up():
    pwm.set_pwm(servo1, 0, servo_actief)
    pwm.set_pwm(servo2, 0, servo_actief)
    pwm.set_pwm(servo3, 0, servo_actief)
    pwm.set_pwm(servo4, 0, servo_actief)
    pwm.set_pwm(servo5, 0, servo_actief)


def all_servos_down():
    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)
    pwm.set_pwm(servo4, 0, servo_rust)
    pwm.set_pwm(servo5, 0, servo_rust)


def random_servo():
    global perv_random_target
    while True:
        random_target = randint(0, 4)
        if random_target != perv_random_target:
            perv_random_target = random_target
            return random_target


def game():
    # puten
    geraakt = 0

    all_servos_down()
    time.sleep(1)
    all_servos_up()
    time.sleep(1)
    all_servos_down()

    tijd_limiet = 30  # aantal seconde dat er gespeeld kan worden
    start_tijd = time.time()  # start tijd is de actueele tijd van nu
    while True:  # loop altijd
        gespeeld_tijd = time.time() - start_tijd  # berekening gespeelde tijd

        if gespeeld_tijd >= tijd_limiet:  # als gespeelde tijd groter is dan tijd limiet stop de loop
            break

        random_target = random_servo()

        if random_target == 0:
            pwm.set_pwm(servo1, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor1):
                    pwm.set_pwm(servo1, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 1:
            pwm.set_pwm(servo2, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor2):
                    pwm.set_pwm(servo2, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 2:
            pwm.set_pwm(servo3, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor3):
                    pwm.set_pwm(servo3, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 3:
            pwm.set_pwm(servo4, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor4):
                    pwm.set_pwm(servo4, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 4:
            pwm.set_pwm(servo5, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor5):
                    pwm.set_pwm(servo5, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

    all_servos_up()
    time.sleep(1)
    all_servos_down()

    distance_player = int(afstand_meting())
    punten_vermenigvuldiging = punten_nomering_cal(distance_player)

    totaalscore = int(geraakt) * int(punten_vermenigvuldiging)

    tijd = now.strftime("%Y-%m-%d %H:%M")

    score_list_add(session["user_id"], totaalscore,
                   geraakt, distance_player, punten_vermenigvuldiging, tijd)


def game_rfid():
    # puten
    geraakt = 0

    all_servos_down()
    time.sleep(1)
    all_servos_up()
    time.sleep(1)
    all_servos_down()

    tijd_limiet = 30  # aantal seconde dat er gespeeld kan worden
    start_tijd = time.time()  # start tijd is de actueele tijd van nu
    while True:  # loop altijd
        gespeeld_tijd = time.time() - start_tijd  # berekening gespeelde tijd

        if gespeeld_tijd >= tijd_limiet:  # als gespeelde tijd groter is dan tijd limiet stop de loop
            break

        random_target = random_servo()

        if random_target == 0:
            pwm.set_pwm(servo1, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor1):
                    pwm.set_pwm(servo1, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 1:
            pwm.set_pwm(servo2, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor2):
                    pwm.set_pwm(servo2, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 2:
            pwm.set_pwm(servo3, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor3):
                    pwm.set_pwm(servo3, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 3:
            pwm.set_pwm(servo4, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor4):
                    pwm.set_pwm(servo4, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if random_target == 4:
            pwm.set_pwm(servo5, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor5):
                    pwm.set_pwm(servo5, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

    all_servos_up()
    time.sleep(1)
    all_servos_down()

    distance_player = int(afstand_meting())
    punten_vermenigvuldiging = punten_nomering_cal(distance_player)

    totaalscore = int(geraakt) * int(punten_vermenigvuldiging)

    score_list_add(3, totaalscore, geraakt, distance_player,
                   punten_vermenigvuldiging, now.strftime("%Y-%m-%d %H:%M"))


def game_active_check():
    with open(account_file, "r") as f:
        lines = f.readlines()
        f.close()
    return lines


def game_activate():
    with open(account_file, "r") as f:
        lines = f.readlines()
        f.close()

    with open(account_file, "w") as f:
        for line in lines:
            if line.strip("\n") != "0":
                f.write(line)

        f.write("1")
        f.close()


def game_deactiveate():
    with open(account_file, "r") as f:
        lines = f.readlines()
        f.close()

    with open(account_file, "w") as f:
        for line in lines:
            if line.strip("\n") != "1":
                f.write(line)

        f.write("0")
        f.close()
