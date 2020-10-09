import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

HitPin = 15

LOM1 = 2  # LOM = Laserontvangermodule
LOM2 = 3
LOM3 = 4
LOM4 = 17
LOM5 = 27

servo1 = 0
servo2 = 5
servo3 = 6
servo4 = 13
servo5 = 19

GPIO.setup(LOM1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pin = GPIO.PWM(HitPin, 50)  # The GPIO pin dat aangestuurd moet worden, signaal frequentie
pin.start(2.5)
