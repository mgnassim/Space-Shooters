# Import de pins hun posities
import RPi.GPIO as GPIO
#Import een library
from mfrc522 import SimpleMFRC522

# Maakt een variable van de rfid
reader = SimpleMFRC522()

try:
        print("Scan de RFID om te spelen!")
        #readerWaarde leest af van reader.read de id van de tag
        readerWaarde = reader.read()
        #Dit doet wanneer er gescanned wordt en deze tag er echt bij hoort
        #dat het dan uitvoert wat er in de if staat.
        if readerWaarde[0] == 1093379580815:
                print("Welkom bij Space Shooters!")

# Finally betekent dat het de code toch uitvoert
# maakt niet uit of try/except false of true is.
finally:
        GPIO.cleanup()

