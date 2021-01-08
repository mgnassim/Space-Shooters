import mysql.connector
from general_background.users import user_create, scoreboard_score, scores
from flask import session

database = mysql.connector.connect(
    host="oege.ie.hva.nl",
    user="mengatn",
    password="A94VSAuJC/JW2J",
    database="zmengatn"
)


def username_list_create():
    user = user_create()
    users = []
    cursor = database.cursor()
    cursor.execute("SELECT `userID`, `username`, `wachtwoord`, `email`, `login`  FROM `User`;")

    result = cursor.fetchall()
    for row in result:
        users.append(user(id=str(row[0]), username=str(row[1]), password=str(row[2]), email=str(row[3]),
                          logins=int(str(row[4]))))
    

    cursor.close()
    return users


def score_list_create():
    score = scores()
    score_list = []
    cursor = database.cursor()
    cursor.execute("SELECT `userID`, `totaalscore`, `geraakt`, `afstand_speler`, `punten_nomering` FROM `Score`;")

    result = cursor.fetchall()
    for row in result:
        score_list.append(score(id=str(row[0]), username=str(row[1]), password=str(row[2]), email=str(row[3]),
                          logins=int(str(row[4]))))

    cursor.close()
    return score_list   


def rfid_codes_create():
    rfid_codes = []
    cursor = database.cursor()
    cursor.execute("SELECT `RFID_CODE` FROM `RFID`;")

    result = cursor.fetchall()
    for row in result:
        rfid_codes.append(str(row[0]))

    cursor.close()
    return rfid_codes


def username_list_add(number_of_users, username, wachtwoord, email):
    cursor = database.cursor()
    new_user = ("INSERT INTO User "
                    "(`userID`, `username`, `wachtwoord`, `email`, `login`)"
                    "VALUES (%s, %s, %s, %s, %s)")

    data_new_user = (number_of_users, username, wachtwoord, email, 0)

    cursor.execute(new_user, data_new_user)
    database.commit()

    cursor.close()


def score_list_add(user_id, totaalscore, geraakt, afstand_speler, punten_normering, tijd):
    cursor = database.cursor()
    new_score = ("INSERT INTO Score "
                    "(`totaalscore`, `geraakt`, `afstand_speler`, `punten_normering`, `userID`, `tijd`)"
                    "VALUES (%s, %s, %s, %s, %s, %s)")

    data_new_score = (totaalscore, geraakt, afstand_speler, punten_normering, user_id, tijd)

    cursor.execute(new_score, data_new_score)
    database.commit()

    cursor.close()


def rfid_codes_add(rfid_code):
    cursor = database.cursor()
    new_rfid = ("INSERT INTO RFID (`RFID_CODE`) VALUES (%s)")

    data_new_rfid = (rfid_code)

    cursor.execute(new_rfid, data_new_rfid)
    database.commit()

    cursor.close()


def password_update(wachtwoord, user_login):
    cursor = database.cursor()
    update_user = "UPDATE `User` SET `User`.`wachtwoord` = %s WHERE `User`.`userid` = %s"

    data_update_user = (wachtwoord, user_login.userid)

    cursor.execute(update_user, data_update_user)
    database.commit() 

    cursor.close()

def logins_update(user_login):
    logins_new = user_login.logins + 1
    cursor = database.cursor()
    update_user = "UPDATE `User` SET `User`.`login` = %s WHERE `User`.`userid` = %s AND `User`.`login` = %s"

    data_update_user = (logins_new, user_login.id, user_login.logins)

    cursor.execute(update_user, data_update_user)
    database.commit()

    cursor.close()

def nieuwste_score():
    cursor = database.cursor(buffered=True)
    cursor.execute("SELECT `totaalscore`, `geraakt`, `afstand_speler`, `punten_normering`, `tijd` FROM `Score` ORDER BY `scoreID` DESC;")

    result = cursor.fetchone()

    cursor.close()
    return result 

def score_list():
    score_lijst = []
    cursor = database.cursor(buffered=True)
    cursor.execute("SELECT `Score`.`totaalscore`, `User`.`username` FROM `User`"
        "INNER JOIN `Score` ON `User`.`userID` = `Score`.`userID` ORDER BY `totaalscore` DESC;")

    result = cursor.fetchmany(20)

    for row in result:
        score_lijst.append("\n" + "\t Player: " + row[1] + "\t score: " + str(row[0]))

    cursor.close()
    return score_lijst 

def score_list_personal():
    user_id = session["user_id"]
    score_lijst_personal = []
    cursor = database.cursor(buffered=True)
    cursor.execute("SELECT `Score`.`totaalscore`, `User`.`userID`, `Score`.`tijd` FROM `User`"
        "INNER JOIN `Score` ON `User`.`userID` = `Score`.`userID` ORDER BY `totaalscore` DESC;")

    result = cursor.fetchall()

    for row in result:
        print("userid" + user_id)
        print("row1" + str(row[1]))
        if int(user_id) == int(row[1]):
            score_lijst_personal.append("\n" + "\t score: " + str(row[0]) + "\t Tijd: " + str(row[2]))

    print(score_lijst_personal)
    cursor.close()
    return score_lijst_personal 