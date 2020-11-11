import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering
GPIO.setwarnings(False)
TRIG = 23                                  #Associate pin 16 to TRIG
ECHO = 24                                  #Associate pin 18 to ECHO

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

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

    pulse_duration = pulse_end - pulse_start                      # bereken de pulse looptijd

    distance = (pulse_duration * 24300)/2                         # vermenigvuldig met de sonische snelheid (34300 cm/s :2 ) omdat heen en weer
    distance = round(distance, 2)
    return distance

if __name__ == '__main__':
    while True:
        print("Distance:", afstand() - 0.5, "cm")  # Print distance with 0.5 cm calibration