import pandas as pd
import classes

users_control = {}


def menu():
    home = int(input('Chose one of the options bellow:\n'
                     '1) Type one to register in the plataform\n'
                     '2) Type two to check the registered users\n'
                     '3) Type three to register a new movie\n'
                     '4) Type four to check the registered movies\n'
                     '5) Type five to recive a new film indication'))

    if home == 1:
        register_user()
    elif home == 2:
        check_users()
    elif home == 3:
        register_movie()
    else:
        print('Invalid option')
        menu()


def register_user():
    name = input("Type your name: ")
    last_name = input('Type your last name: ')
    age = input("Type your age: ")
    sex = input("Type your sex: ")
    user = classes.User()


def check_users():
    pass


def register_movie():
    pass


def check_movies():
    pass


def indicate_film():
    pass


menu()
