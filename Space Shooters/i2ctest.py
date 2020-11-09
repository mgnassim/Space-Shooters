from __future__ import division
import RPi.GPIO as GPIO
import time


# Import the PCA9685 module.
import Adafruit_PCA9685
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)#pin 4 is input van sesnor 1
GPIO.setup(27, GPIO.IN)#pin 4 is input van sesnor 1
Sensor1 = 4
Sensor2 = 27


# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 350  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 50       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_min)
    pwm.set_pwm(1, 0, servo_min)
    time.sleep(1)
    if GPIO.input(Sensor1):
        pwm.set_pwm(0, 0, servo_max)
        time.sleep(1)
    if GPIO.input(Sensor2):
        pwm.set_pwm(1, 0, servo_max)
        time.sleep(1)