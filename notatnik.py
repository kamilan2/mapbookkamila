users: list = [

    {"name": "Julia", "surname": "Gotowiec", "posts": 1500, },
    {"name": "Hubert", "surname": "Sybilski", "posts": 123456, },
    {"name": "Adrian", "surname": "Dobrzan", "posts": 2137, },
    {"name": "Bartek", "surname": "Wyrzychowski", "posts": 300, }
]

def update_user(users: list):
    imie =input("Wprowadź imie uzytkownika, ktorego dane chccesz zmienic: ")
    for user in users:
        if user["name"] == imie:
            user["name"] = input("Podaj nowe imie: ")
            user["surname"] = input("Podaj nowe nazwisko: ")
            user["posts"] = int(input("Podaj nowa liczbe postow: "))

update_user(users)
print(users)