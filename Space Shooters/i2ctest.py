from __future__ import division                            # Helpt bij het jet importen zorgt voor geen verwaring

import RPi.GPIO as GPIO                                     # Import library GPIO

import time,threading                                       # Import library Time.

import Adafruit_PCA9685                                     # Import library van PCA9685 module.

GPIO.setmode(GPIO.BCM)                                      # Aangeven welke type pin notering er gebruikt word
GPIO.setwarnings(False)                                     # Zet waarschuwing uit

#instelling voor ontvangers
Sensor1 = 4
Sensor2 = 27
Sensor3 = 5

GPIO.setup(Sensor1, GPIO.IN)                                 # Pin als input voor sensor 1
GPIO.setup(Sensor2, GPIO.IN)                                 # Pin als  input vor sensor 2
GPIO.setup(Sensor3, GPIO.IN)                                 # Pin 5 is input van sensor 3


#Instelling voor afstand sensor

TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)                                   # Set pin als GPIO out
GPIO.setup(ECHO,GPIO.IN)                                    # Set pin als GPIO in

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
    return distance




if __name__ == '__main__':

    pwm = Adafruit_PCA9685.PCA9685()                        # Initialiseer de PCA9685 met het standaardadres (basis adddres 0x40).

    pwm.set_pwm_freq(50)                                    # Verander de PWM frequentrie naar 50MHZ

    # Hier configureer ik de minimaale en maximaale waardes voor de pulse
    servo_min = 100  # Min pulse length out of 4096
    servo_max = 350  # Max pulse length out of 4096 (90 graden)
    servo1 = 15
    servo2 = 0
    servo3 = 12

    print('press Ctrl-C to quit...')

    pwm.set_pwm(servo1, 0, servo_min)                                             #draao90graden
    pwm.set_pwm(servo2, 0, servo_min)                                             #draao90graden
    pwm.set_pwm(servo3, 0, servo_min)                                             #draao90graden
    time.sleep(1)

    #score instelling
    punten = 0
    punten_nomering =0
    gemiddeldetijd=0
    totaalscore=0


    tijd_limiet = 30                                                          #aantal minuten dat er gespeeld kan worden
    start_tijd = time.time()                                                  #start tijd is de actueele tijd van nu
    while True:                                                               #loop altijd
        gespeeld_tijd = time.time() - start_tijd                              #berekening gespeelde tijd

         # Als de if waarde true is word word de statement uitgevoerd

        if gespeeld_tijd > tijd_limiet:                                      #als gespeelde tijd groter is dan tijd limiet stop de loop
            break

        if GPIO.input(Sensor1):                                              #als een sensor iets onvangt(true) doe dan dit
            punten = punten+1                                                #punten +1
            pwm.set_pwm(servo1, 0, servo_max)                                #Beweeg servo
            time.sleep(1)                                                    #wacht 1 sec
            pwm.set_pwm(servo1, 0, servo_min)                                #beweeg servo

        if GPIO.input(Sensor2):
            punten = punten+1
            pwm.set_pwm(servo2, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(servo2, 0, servo_min)

        if GPIO.input(Sensor3):
            punten = punten+1
            pwm.set_pwm(servo3, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(servo3, 0, servo_min)

        if afstand() < 10:
            punten_nomering = 0

        if afstand() > 10 and afstand() < 30:
            punten_nomering = 1

        if afstand() > 30 and afstand() < 50:
            punten_nomering = 2

        if afstand() > 50 and afstand() < 100:
            punten_nomering = 3

        if afstand() > 100:
            punten_nomering = 4



    pwm.set_pwm(servo1, 0, servo_max)                                       #draai naar thuispositie
    pwm.set_pwm(servo2, 0, servo_max)                                       #draai naar thuispositie
    pwm.set_pwm(servo3, 0, servo_max)                                       #draai naar thuispositie
    time.sleep(1)

    print('game over')

    totaalscore = punten * punten_nomering
    print(totaalscore)
    print(afstand())
    print('targets geraakt '+punten+' score is '+totaalscore+' nomering ' +punten_nomering)
    print(totaalscore)

