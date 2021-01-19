from flask import Blueprint, render_template, redirect, url_for, g, request
import Adafruit_PCA9685  # Import library van PCA9685 module.
import RPi.GPIO as GPIO  # Import library GPIO

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servo_actief = 100
servo_rust = 350


def servo1_test():
    sensor = 4
    GPIO.setup(sensor, GPIO.IN)

    servo = 15
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('admin.admin_web'))


def servo2_test():
    sensor = 5
    GPIO.setup(sensor, GPIO.IN)

    servo = 12
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('admin.admin_web'))


def servo3_test():
    sensor = 17
    GPIO.setup(sensor, GPIO.IN)

    servo = 7
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('admin.admin_web'))


def servo4_test():
    sensor = 22
    GPIO.setup(sensor, GPIO.IN)

    servo = 1
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('admin.admin_web'))


def servo5_test():
    sensor = 27
    GPIO.setup(sensor, GPIO.IN)

    servo = 0
    pwm.set_pwm(servo, 0, servo_actief)

    while True:
        if GPIO.input(sensor):
            pwm.set_pwm(servo, 0, servo_rust)
            return redirect(url_for('admin.admin_web'))
