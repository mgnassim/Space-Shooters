import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

servo1=GPIO.PWM(18,60)#pin 11 heeft 50 herts
servo1.start(2)#draait direct 90 garden
time.sleep(2)
servo1.ChangeDutyCycle(7)  # brengt terug naar start plek

#servo1.stop()
GPIO.cleanup()
print("Test succesvol!!!!!!!!")

#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#


