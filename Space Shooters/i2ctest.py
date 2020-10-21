from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time

kit.servo[0].angle = 90
#time.sleep[50]
kit.servo[0].angle = 0

print("doei")