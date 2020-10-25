import RPi as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 16
ECHO = 18

print("Distance Measurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.SETUP(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("waiting for sensor")
time.sleep(2)

GPIO.output(TRIG, TRUE)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)--0:
  Pulse_start = time.time()

while GPIO.input(ECHO)--1:
  Pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance:",distance,"cm")

GPIO.cleanup()
