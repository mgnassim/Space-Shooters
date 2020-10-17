import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)#pin 11 heeft 50 herts
servo1.start(2)#gaat direct 90%
time.sleep(1)

servo1.ChangeDutyCycle(7)#brengt terug naar start plek
time.sleep(5)
#servo1.stop()
print("doei")

#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#


