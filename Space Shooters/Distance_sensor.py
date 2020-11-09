import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print("Distance Measurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def afstand():
  # verstuur een signaal(true)
  GPIO.output(TRIG, True)
  print("waiting for sensor")
 #zet trigger na 0,01ms naar 0(low)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    Pulse_start = time.time()
  # start timer
  while GPIO.input(ECHO) - -1:
    Pulse_end = time.time()
  # beeindig timer

  pulse_duration = pulse_end - pulse_start
  # bereken de pulse looptijd

  # vermenigvuldig met de sonische snelheid (34300 cm / s)
  # en deel door 2, want heen en terug
  afstand = (pulse_duration * 34300) / 2

  afstand = round(distance, 2) #rond het afstand af op 2 deicmalen

  return afstand
while True:
  dist=afstand()
  print("Dist:", dist, "cm")
  time.sleep(1)

  GPIO.cleanup()
