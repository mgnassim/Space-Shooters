import mysql.connector
from general_background.users import user_create, scores

database = mysql.connector.connect(
    host="oege.ie.hva.nl",
    user="grootbj2",
    password="Dpe#aEN8YQ2mkV",
    database="zgrootbj2"
)


def username_list_create():
    user = user_create()
    users = []
    cursor = database.cursor()
    cursor.execute("SELECT `UserID`, `Username`, `Wachtwoord`, `Email`, `Logins`  FROM `FysUsers`;")

    result = cursor.fetchall()
    for row in result:
        users.append(user(id=str(row[0]), username=str(row[1]), password=str(row[2]), email=str(row[3]),
                          logins=int(str(row[4]))))

    cursor.close()
    database.close()
    return users


def score_list_create():
    score = scores()
    score_list = []
    cursor = database.cursor()
    cursor.execute("SELECT `UserID`, `totaalscore`, `geraakt`, `afstand_speler`, `punten_nomering`, `gem_tijd`, `tijd` "
                   "FROM `FysScores`;")

    result = cursor.fetchall()
    for row in result:
        score_list.append(score(id=str(row[0]), username=str(row[1]), password=str(row[2]), email=str(row[3]),
                          logins=int(str(row[4]))))

    cursor.close()
    database.close()
    return score_list


def rfid_codes_create():
    rfid_codes = []
    cursor = database.cursor()
    cursor.execute("SELECT `RfidCodes` FROM `FysRfid`;")

    result = cursor.fetchall()
    for row in result:
        rfid_codes.append(str(row[0]))

    cursor.close()
    database.close()
    return rfid_codes


def username_list_add(number_of_users, username, wachtwoord, email):
    cursor = database.cursor()
    new_user = ("INSERT INTO FysUsers "
                    "(`UserID`, `Username`, `Wachtwoord`, `Email`, `Logins`)"
                    "VALUES (%s, %s, %s, %s, %s)")

    data_new_user = (number_of_users, username, wachtwoord, email, "0")

    cursor.execute(new_user, data_new_user)
    database.commit()

    cursor.close()
    database.close()


def score_list_add(userid, totaalscore, geraakt, afstand_speler, punten_nomering, gem_tijd, tijd):
    cursor = database.cursor()
    new_score = ("INSERT INTO FysScores "
                    "(`UserID`, `totaalscore`, `geraakt`, `afstand_speler`, `punten_nomering`, `gem_tijd`, `tijd`)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    data_new_score = (userid, totaalscore, geraakt, afstand_speler, punten_nomering, gem_tijd, tijd)

    cursor.execute(new_score, data_new_score)
    database.commit()

    cursor.close()
    database.close()


def rfid_codes_add(rfid_code):
    cursor = database.cursor()
    new_rfid = ("INSERT INTO FysRfid (`rfid_code`) VALUES (%s)")

    data_new_rfid = (rfid_code)

    cursor.execute(new_rfid, data_new_rfid)
    database.commit()

    cursor.close()
    database.close()


def password_update(wachtwoord, user_login):
    cursor = database.cursor()
    update_user = "UPDATE FysUsers SET Wachtwoord = %s WHERE Wachtwoord = %s"

    data_update_user = (user_login.wachtwoord, wachtwoord)

    cursor.execute(update_user, data_update_user)
    database.commit()

    cursor.close()
    database.close()

