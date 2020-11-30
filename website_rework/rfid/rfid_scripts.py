from mfrc522 import SimpleMFRC522

rfid_codes = (
    "../website_rework/text_files/RFID_Codes.txt"
)

game_active = (
    "../website_rework/text_files/game_active.txt"
)


def rfid_scan():
    # rfid reader
    reader = SimpleMFRC522()
    reader_waarde = reader.read()
    return reader_waarde[0]


def pas_number_inject():
    global rfid_codes
    code = open(rfid_codes, "r")
    return code
