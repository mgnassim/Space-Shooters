from user.game.game_script import game_rfid, game_activate, game_deactiveate, game_active_check
from rfid.rfid_scripts import rfid_scan, pas_number_inject

while True:
    if rfid_scan() == pas_number_inject():
        if game_active_check() == 0:
            game_activate()
            game_rfid()
            game_deactiveate()
