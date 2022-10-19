import pandas as pd
import classes

users_control = {'Name': [],
                 'Last Name': [],
                 'Age': [],
                 'Sex': [],
                 }

movie_control = {"Name": [],
                 "Genre": [],
                 "Year": [],
                 "Minimum Age": []}


def menu():
    home = int(input('Chose one of the options bellow:\n'
                     '1) Type one to register in the plataform\n'
                     '2) Type two to check the registered users\n'
                     '3) Type three to register a new movie\n'
                     '4) Type four to check the registered movies\n'
                     '5) Type five to recive a new film indication\n'
                     '6) Exit the system\n'
                     '-> '))

    if home == 1:
        register_user()
    elif home == 2:
        check_users()
    elif home == 3:
        register_movie()
    elif home == 4:
        check_movies()
    elif home == 5:
        indicate_movie()
    elif home == 6:
        exit()
    else:
        print('Invalid option')
        menu()


def register_user():
    name = str(input("Type your name: "))
    last_name = str(input('Type your last name: '))
    age = int(input("Type your age: "))
    sex = str(input("Type your sex: "))

    # Creating a variable user
    user = classes.User(name=name, last_name=last_name, age=age, sex=sex)

    # Adding this user to my spreadsheet
    users_control['Name'].append(name)
    users_control['Last Name'].append(last_name)
    users_control['Age'].append(age)
    users_control['Sex'].append(sex)
    print("You've ben add to the system")
    print(users_control)
    menu()


def check_users():
    print(pd.DataFrame(users_control))
    menu()


def register_movie():
    name = str(input("Type the name of the movie: "))
    genre = str(input("Type the genre of the movie: "))
    year = int(input("Type the year of the movie: "))
    minimum_age = int(input("Type the minimum age user permitted: "))

    # Creating the movie
    movie = classes.Movie(name=name, genre=genre, year=year, minimum_age=minimum_age)

    # Adding the movie in to the spreadsheet
    movie_control['Name'].append(name)
    movie_control['Genre'].append(genre)
    movie_control['Year'].append(year)
    movie_control['Minimum Age'].append(minimum_age)
    print("Your movie has been added")
    menu()


def check_movies():
    print(pd.DataFrame(movie_control))


def indicate_movie():
    pass


menu()
