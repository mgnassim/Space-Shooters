import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)#pin 4 is input van sesnor 1
GPIO.setup(17, GPIO.IN)#pin 17 is input van sesnor 1
GPIO.setup(27, GPIO.IN)#pin 11 is input van sesnor 1
GPIO.setup(22, GPIO.IN)#pin 11 is input van sesnor 1
GPIO.setup(5, GPIO.IN)#pin 11 is input van sesnor 1
Sensor1 = 4
Sensor2 = 17
Sensor3 = 27
Sensor4 = 22
Sensor5 = 5

while True:
    if GPIO.input(Sensor1):  # if port 11 == 1
        print("Port 4 is 1/GPIO.HIGH/True")
        #time.sleep(1)
    if GPIO.input(Sensor2):  # if port 11 == 1
        print("Port 17 is 1/GPIO.HIGH/True")
        #time.sleep(1)
    if GPIO.input(Sensor3):  # if port 11 == 1
        print("Port 27 is 1/GPIO.HIGH/True")
        #time.sleep(1)
    if GPIO.input(Sensor4):  # if port 11 == 1
        print("Port 22 is 1/GPIO.HIGH/True")
        #time.sleep(1)
    if GPIO.input(Sensor5):  # if port 11 == 1
        print("Port 5 is 1/GPIO.HIGH/True")
        #time.sleep(1)