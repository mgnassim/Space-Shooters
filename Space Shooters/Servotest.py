import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)#pin 11 heeft 50 herts
servo1.start(2)
time.sleep(1)

servo1.ChangeDutyCycle(12)#rechts
time.sleep(1)
pwm.stop()
print("doei")

#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)



