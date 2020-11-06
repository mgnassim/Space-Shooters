import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print("Distance Measurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)



GPIO.output(TRIG,True)
print("waiting for sensor")
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)--0:
  Pulse_start = time.time()
#start timer
while GPIO.input(ECHO)--1:
  Pulse_end = time.time()
#beeindig timer

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance:",distance,"cm")

GPIO.cleanup()
