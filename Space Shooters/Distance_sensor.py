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
  GPIO.output(TRIG, False)                         # naar 0(low)
  print ("Waiting Sensor To Settle")
  time.sleep(2)

  GPIO.output(TRIG, True)                          # verstuur een signaal(true)
  print("waiting for sensor")
  time.sleep(0.00001)                              #zet trigger na 0,01ms naar 0(low)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()                      #start timer

  while GPIO.input(ECHO) - -1:
    pulse_end = time.time()                         # beeindig timer

  pulse_duration = pulse_end - pulse_start
  # bereken de pulse looptijd

  # vermenigvuldig met de sonische snelheid (34300 cm / s)
  # en deel door 2, want heen en terug
  afstand = (pulse_duration * 34300) / 2

  afstand = round(afstand, 2) #rond het afstand af op 2 deicmalen

  return afstand

while True:
  print("Afstand = :", afstand(), "cm")
  time.sleep(1)

  GPIO.cleanup()
