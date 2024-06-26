from tkinter import *
import tkintermapview

users=[]

class User:
    def __init__(self, name, surname, posts, location):
        self.name = name
        self.surname = surname
        self.posts = posts
        self.location = location

def lista_uzytkownikow():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{user.name}  {user.surname} {user.posts} {user.location}')

def dodaj_uzytkownika():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    posty = entry_posty.get()
    miejscowosc = entry_miejscowosc.get()
    print(imie, nazwisko, posty, miejscowosc)
    users.append(User(imie, nazwisko, posty, miejscowosc))

    lista_uzytkownikow()

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)

    entry_imie.focus()

def usun_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(i)
    users.pop(i)
    lista_uzytkownikow()

def pokaz_szczegoly_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    imie = users[i].name
    label_imie_szczegoly_obiektu_wartosc.config(text=imie)
    nazwisko = users[i].surname
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
    posty = users[i].posts
    label_posty_szczegoly_obiektu_wartosc.config(text=posty)
    miejscowosc = users[i].location
    label_miejscowosc_szczegoly_obiektu_wartosc.config(text=miejscowosc)

def edytuj_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    entry_imie.insert(0, users[i].name)
    entry_nazwisko.insert(0, users[i].surname)
    entry_posty.insert(0, users[i].posts)
    entry_miejscowosc.insert(0, users[i].location)
    button_dodaj_uzytkownika.config(text="Zapisz zmiany", command= lambda:aktualizuj_uzytkownika(i))

def aktualizuj_uzytkownika(i):
     users[i].imie = entry_imie.get()
     users[i].surname = entry_nazwisko.get()
     users[i].posts = entry_posty.get()
     users[i].location = entry_miejscowosc.get()
     lista_uzytkownikow()
     button_dodaj_uzytkownika.config(text="Dodaj użytkownika", command=dodaj_uzytkownika)
     entry_imie.delete(0, END)
     entry_nazwisko.delete(0, END)
     entry_posty.delete(0, END)
     entry_miejscowosc.delete(0, END)
     entry_imie.focus()


#GUIa
root = Tk()
root.title("MapBook")
root.geometry("1024x760")

# ramki do porządkowania struktury
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

# lista obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista obiektów: ")
listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=50)
button_pokaz_szczegoly = Button(ramka_lista_obiektow, text="Pokaż szczegóły", command=pokaz_szczegoly_uzytkownika)
button_usun_obiekt = Button(ramka_lista_obiektow, text="Usuń obiekt", command=usun_uzytkownika)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text="Edytuj obiekt", command=edytuj_uzytkownika)

label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

# formularz
label_formularz = Label(ramka_formularz, text="Formularz: ")
label_imie = Label(ramka_formularz, text="Imię: ")
label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
label_posty = Label(ramka_formularz, text="Liczba postów: ")
label_miejscowosc = Label(ramka_formularz, text="Miejscowość: ")
button_dodaj_uzytkownika = Button(ramka_formularz, text="Dodaj użytkownika", command=dodaj_uzytkownika)

entry_imie = Entry(ramka_formularz)
entry_nazwisko = Entry(ramka_formularz)
entry_posty = Entry(ramka_formularz)
entry_miejscowosc = Entry(ramka_formularz)

label_formularz.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_posty.grid(row=3, column=0, sticky=W)
label_miejscowosc.grid(row=4, column=0, sticky=W)
button_dodaj_uzytkownika.grid(row=5, column=1, columnspan=2)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)
entry_miejscowosc.grid(row=4, column=1)

# szczegoly uzytkownika

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły użtykownika: ")
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Imię: ")
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Liczba postów: ")
label_miejscowosc_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Miejscowość: ")

label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...", width=10)
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...", width=10)
label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...", width=10)
label_miejscowosc_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...", width=10)

label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
label_imie_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1, sticky=W)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_posty_szczegoly_obiektu.grid(row=1, column=4)
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)
label_miejscowosc_szczegoly_obiektu.grid(row=1, column=6)
label_miejscowosc_szczegoly_obiektu_wartosc.grid(row=1, column=7)

map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=500)
map_widget.set_position(52.2, 21.0)
map_widget.set_zoom(8)

map_widget.grid(row=2, column=0, columnspan=8)
marker_wat = map_widget.set_marker(52.253528201838805, 20.899764798910137, text="WAT")



root.mainloop()
