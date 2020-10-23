import RPi.GPIO as GPIO
import os, time



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)#pin 11 is input can sesnor
SensorGPIO = 7

while True:
    if GPIO.input(SensorGPIO):  # if port 11 == 1
        print("Port 7 is 1/GPIO.HIGH/True")
    else:
        print("Port 7 is 0/GPIO.LOW/False")