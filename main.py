from models.data_source import users
from utils.crud import read_friends, add_user



if __name__ == '__main__':
    while True:
        print("Welcome to the new chose an option")
        print("1. Read a list of friends")
        print("0. Exit")
        print("2. Add new user")
        menu_options = input("Choose an option")
        if menu_options == "0":
            break
        if menu_options == "1":
            read_friends(users)
        if menu_options == "2":
            add_user(users)