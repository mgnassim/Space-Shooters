users = []
account_file = "../website_rework/text_files/accounts.txt"


def user_create():

    # word aan gegeven wat er in de array users komt te staan
    class User:
        def __init__(self, id, username, password, email, logins):
            self.id = id
            self.username = username
            self.password = password
            self.email = email
            self.logins = logins

        def __repr__(self):
            return f'<User: {self.username}>'

    return User


def users_pull_file():
    user = user_create()
    # Het bestand met alle gebruikers word geopend en regel voor regel gelezen
    # Na het lezen van de regel word het gesplitst en in de users array gezet waarna het later terug gevraagd kan worden
    for line in open(account_file, "r").readlines():
        accounts = line.split()
        users.append(
            user(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3], logins=int(accounts[4])))

    return users
