#from __future__ import division                  #helpt bij het jet importen zorgt voor geen verwaring

import RPi.GPIO as GPIO                           # Import library GPIO
import time,threading                             # Import library Time.
import Adafruit_PCA9685                           # Import library van PCA9685 module.
from random import randint

GPIO.setmode(GPIO.BCM)                            # Aangeven welke type pin notering er gebruikt word
GPIO.setwarnings(False)                           # Zet waarschuwing uit

#pinnen instellen
GPIO.setup(4, GPIO.IN)                            # Pin 4 is input van sensor 3
GPIO.setup(27, GPIO.IN)                           # Pin 27 is input van sensor 3
GPIO.setup(5, GPIO.IN)                            # Pin 5 is input van sensor 3


#decaleer ik waarden
Sensor1 = 4
Sensor2 = 5
Sensor3 = 27

#afstandsensor
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)                                   # Set pin als GPIO out
GPIO.setup(ECHO,GPIO.IN)                                    # Set pin als GPIO in

#puten
geraakt = 0
punten_nomering = 0

def afstand():
    GPIO.output(TRIG, False)                                      # Set TRIG as LOW
    time.sleep(2)

    GPIO.output(TRIG, True)                                       # Verstuur een signaal(true)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)                                      # Zet trigger na 0,01ms naar 0(low)

    while GPIO.input(ECHO) == 0:                                  # Check als  de ECHO LOW (0) is
        pulse_start = time.time()                                 # Bewaar de genoteerde tijd van de low pulse

    while GPIO.input(ECHO) == 1:                                  # Check als  de ECHO HIGH (1) is
        pulse_end = time.time()                                   # Bewaar de laatst genoteerde tijd van de low pulse

    pulse_lengte = pulse_end - pulse_start                      # bereken de pulse looptijd

    distance = (pulse_lengte * 24300)/2                         # vermenigvuldig met de sonische snelheid (34300 cm/s :2 ) omdat heen en weer
    distance = round(distance, 2)
    distance = int(distance)
    return distance



if __name__ == '__main__':

    pwm = Adafruit_PCA9685.PCA9685()                      #Initialiseer de PCA9685 met het standaardadres (basis adddres 0x40).

    pwm.set_pwm_freq(50)                                  #Verander de PWM frequentrie naar 50MHZ

    # Hier congigureer ik de minimaale en maximaale waardes voor de pulse
    servo_actief = 100  # Min pulse length out of 4096
    servo_rust = 350  # Max pulse length out of 4096 (90 graden)
    servo1 = 15
    servo2 = 12
    servo3 = 0

    print('press Ctrl-C to quit...')

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_actief)       #draao90graden
    pwm.set_pwm(servo2, 0, servo_actief)       #draao90graden
    pwm.set_pwm(servo3, 0, servo_actief)        #draao90graden

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)

    time.sleep(1)


    tijd_limiet = 30                      #aantal minuten dat er gespeeld kan worden
    start_tijd = time.time()              #start tijd is de actueele tijd van nu
    pervRandomTarget = -1
    while True:                                            #loop altijd
        gespeeld_tijd = time.time() - start_tijd              #berekening gespeelde tijd

        if gespeeld_tijd > tijd_limiet:                                      #als gespeelde tijd groter is dan tijd limiet stop de loop
            break

        while True:
            RandomTarget = randint(0, 2)
            if RandomTarget != pervRandomTarget:
                break

        pervRandomTarget = RandomTarget

        if RandomTarget == 0:
            pwm.set_pwm(servo1, 0, servo_actief)
            while True:
                if GPIO.input(Sensor1):
                    pwm.set_pwm(servo1, 0, servo_rust)
                    geraakt += 1
                    break

        if RandomTarget == 1:
            pwm.set_pwm(servo2, 0, servo_actief)
            while True:
                if GPIO.input(Sensor2):
                    pwm.set_pwm(servo2, 0, servo_rust)
                    geraakt += 1
                    break

        if RandomTarget == 2:
            pwm.set_pwm(servo3, 0, servo_actief)
            while True:
                if GPIO.input(Sensor3):
                    pwm.set_pwm(servo3, 0, servo_rust)
                    geraakt += 1
                    break

    if afstand() < 10:
        punten_nomering = 0

    elif afstand() >= 10 & afstand() <= 30:
        punten_nomering = 1

    elif afstand() >= 30 & afstand() < 50:
        punten_nomering = 2

    elif afstand() >= 50 & afstand() <= 100:
        punten_nomering = 3

    elif afstand() > 100:
        punten_nomering = 4

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
    print('game over')

    totaalscore = geraakt * punten_nomering
    print(totaalscore)
    print(afstand())
    print('targets geraakt ' + geraakt + ' score is ' + totaalscore + ' nomering ' + punten_nomering)
    print(totaalscore)