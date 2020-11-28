from flask import redirect, session, request, url_for
from general_background.users import user_create, users_pull_file

user = user_create()
users = users_pull_file()


def logedin_check():
    if not int(session["user_id"]) >= 1:
        return redirect(url_for("login_backend.login"))


def bubble_sorting():
    highscore_file = "../Website/highscore.txt"

    # lege array gecreërd om daar daarna alle variabelen in te doen om daarna te gaan sorteren
    array_refomate = []

    # het bestand highscore.txt word geopend om er in te lezen aangegeven door de "r". het word regel voor regel
    # gelezen. Elke regel word appart van elkaar in het varariable scorebord gezet. Waarna het zich split en de naam en
    # score er alleen uitpakt en het dan formateerd: "score naam". waarna het word in array_refomate word gezet.
    for line in open(highscore_file, "r").readlines():
        scorebord = line.split()
        array_refomate.append(scorebord[1] + " " + scorebord[0])

    # er word gemeten hoelang de array is in array_refomate.
    n = len(array_refomate)

    # Dit is een loop dat even vaak rond gaat als de array lang is. Om de array te gaan sorteren als een bubbel sort.
    # https://en.wikipedia.org/wiki/Bubble_sort
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array_refomate[j] > array_refomate[j + 1]:
                array_refomate[j], array_refomate[j + 1] = array_refomate[j + 1], array_refomate[j]

                already_sorted = False

        if already_sorted:
            break

    array_refomate.reverse()
    return array_refomate
