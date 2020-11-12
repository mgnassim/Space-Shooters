# Import de pins hun posities
import RPi.GPIO as GPIO
#Import een library
from mfrc522 import SimpleMFRC522

# Maakt een variable van de rfid
reader = SimpleMFRC522()

try:
        text = input('New Data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
        id, text = reader.read()
        print(id)
        print(text)

# Finally betekent dat het de code toch uitvoert
# maakt niet uit of try/except false of true is.
finally:
        GPIO.cleanup()
