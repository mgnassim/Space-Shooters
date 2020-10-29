import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11,50) # GPIO 11  with 50Hz
p.start(2) # Initialization
time.sleep(2)
p.ChangeDutyCycle(8)
time.sleep(2)

p.stop()