import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)


servo1=GPIO.PWM(11,50)#pin 11 heeft 50 herts
servo1.start(2)#draait direct 90 garden
servo1.ChangeDutyCycle(6)  # brengt terug naar start plek
#servo1.ChangeDutyCycle(0)


#servo1.stop()
GPIO.cleanup()
print("Test succesvol!!!!!!!!")

#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#