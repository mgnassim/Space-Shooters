import RPi.GPIO as GPIO  # Import library GPIO
from mfrc522 import SimpleMFRC522

from user.game.game_script import game_rfid

GPIO.setwarnings(False)


if __name__ == '__main__':

    while True:
        print('scan je pas')
        # rfid reader
        reader = SimpleMFRC522()
        pas = 287538782903
        readerWaarde = reader.read()

        if readerWaarde[0] == pas:
            game_rfid()
