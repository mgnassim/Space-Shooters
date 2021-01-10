from user.game.game_script import game_rfid, game_activate, game_deactiveate, game_active_check
from rfid.rfid_scripts import rfid_scan
from database.database import pas_nummers


def rfid():
    while True:
        if rfid_scan() in pas_nummers():
            if game_active_check == 0:
                game_activate()
                game_rfid()
                game_deactiveate()
