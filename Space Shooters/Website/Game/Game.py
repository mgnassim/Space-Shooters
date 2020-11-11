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
Sensor2 = 27
Sensor3 = 5




if __name__ == '__main__':

    pwm = Adafruit_PCA9685.PCA9685()                      #Initialiseer de PCA9685 met het standaardadres (basis adddres 0x40).

    pwm.set_pwm_freq(50)                                  #Verander de PWM frequentrie naar 50MHZ

    # Hier congigureer ik de minimaale en maximaale waardes voor de pulse
    servo_min = 100  # Min pulse length out of 4096
    servo_max = 350  # Max pulse length out of 4096 (90 graden)

    print('press Ctrl-C to quit...')

    pwm.set_pwm(15, 0, servo_max)
    pwm.set_pwm(12, 0, servo_max)
    pwm.set_pwm(0, 0, servo_max)

    time.sleep(1)

    pwm.set_pwm(15, 0, servo_min)       #draao90graden
    pwm.set_pwm(12, 0, servo_min)       #draao90graden
    pwm.set_pwm(0, 0, servo_min)        #draao90graden

    time.sleep(1)

    pwm.set_pwm(15, 0, servo_max)
    pwm.set_pwm(12, 0, servo_max)
    pwm.set_pwm(0, 0, servo_max)

    time.sleep(1)


    tijd_limiet = 30                      #aantal minuten dat er gespeeld kan worden
    start_tijd = time.time()              #start tijd is de actueele tijd van nu
    pervRandomTarget = -1
    while True:                                            #loop altijd
        gespeeld_tijd = time.time() - start_tijd              #berekening gespeelde tijd

        while True:
            RandomTarget = randint(0, 2)
            if RandomTarget != pervRandomTarget:
                break

        pervRandomTarget = RandomTarget

        if RandomTarget == 0:
            pwm.set_pwm(15, 0, servo_max)
            while True:
                pwm.set_pwm(15, 0, servo_min)
                break

        if RandomTarget == 1:
            pwm.set_pwm(0, 0, servo_max)
            while True:
                pwm.set_pwm(0, 0, servo_min)
                break

        if RandomTarget == 2:
            pwm.set_pwm(12, 0, servo_max)
            while True:
                pwm.set_pwm(12, 0, servo_min)
                break

        print('game over')
        pwm.set_pwm(15, 0, servo_max)
        pwm.set_pwm(12, 0, servo_max)
        pwm.set_pwm(0, 0, servo_max)
        time.sleep(1)