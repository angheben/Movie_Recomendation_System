class User:
    def __init__(self, name, last_name, age, sex):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"{self.name + self.last_name} have {self.age} and it's {self.sex}"


class Movie:
    def __init__(self, name, genre, year, minimum_age):
        self.name = name
        self.genre = genre
        self.year = year
        self.minimum_age = minimum_age

    def __str__(self):
        return f"The movie {self.name} it's of the genre {self.genre} was prduced in {self.year} and have it's "\
               f"permited to people with the minimum age of {self.minimum_age} years old"

