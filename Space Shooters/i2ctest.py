from __future__ import division
import RPi.GPIO as GPIO
import time ,threading


# Import the PCA9685 module.
import Adafruit_PCA9685
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)#pin 4 is input van sesnor 1
GPIO.setup(27, GPIO.IN)#pin 27 is input van sesnor 1
GPIO.setup(5, GPIO.IN)#pin 5 is input van sesnor 1
Sensor1 = 4
Sensor2 = 27
Sensor3 = 5


# Initialise the PCA9685 using the default address (0x40).

def foo():
    print(time.ctime())
    threading.Timer(3600, foo).start()
    if threading.Timer(3600):


if __name__ == '__main__':

    pwm = Adafruit_PCA9685.PCA9685()

    # Configure min and max servo pulse lengths
    servo_min = 100  # Min pulse length out of 4096
    servo_max = 350  # Max pulse length out of 4096 (90 graden)

    pwm.set_pwm_freq(50)

    print('press Ctrl-C to quit...')

    pwm.set_pwm(15, 0, servo_min)
    time.sleep(1)
    while True:
        # Move servo on channel O between extremes.

        if GPIO.input(Sensor1):
            pwm.set_pwm(15, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(15, 0, servo_min)

        if GPIO.input(Sensor2):
            pwm.set_pwm(0, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(0, 0, servo_min)
        if GPIO.input(Sensor3):
            pwm.set_pwm(12, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(12, 0, servo_min)