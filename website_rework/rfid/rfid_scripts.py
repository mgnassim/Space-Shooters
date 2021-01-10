from mfrc522 import SimpleMFRC522


def rfid_scan():
    # rfid reader
    reader = SimpleMFRC522()
    reader_waarde = reader.read()
    return reader_waarde[0]