def read_friends(users: list)->None:
    print("informacje o Twoich znajomych: ")
    for user in users:
        print(f'\tTwoj znajomy {user["name"]} {user["surname"]} opublikowal {user["posts"]} postow.')

def add_user(lista: list) -> None:
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_postow = int(input("Podaj liczbę postów uzytkownika: "))
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow, }
    lista.append(new_user)

def search_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            print(users)


def remove_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            users.remove(user)

def update_user(users: list):
    imie =input("Wprowadź imie uzytkownika, ktorego dane chccesz zmienic: ")
    for user in users:
        if user["name"] == imie:
            user["name"] = input("Podaj nowe imie: ")
            user["surname"] = input("Podaj nowe nazwisko: ")
            user["posts"] = int(input("Podaj nowa liczbe postow: "))