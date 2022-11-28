from connection import *
from cart import *
from db import *


class Klient:
    def __init__(self, login) -> None:
        self.login = login
        self.koszyk = Koszyk(login)
        self.imie = self.daneUzytkownika()[0]
        self.nazwisko = self.daneUzytkownika()[1]
        self.email = self.daneUzytkownika()[2]
        self.nrTel = self.daneUzytkownika()[3]
        self.miasto = self.daneUzytkownika()[4]
        self.ulica = self.daneUzytkownika()[5]
        self.lokal = self.daneUzytkownika()[6]
        self.kodPocztowy = self.daneUzytkownika()[7]
        self.type = "user"
        self.wypiszDane()

    def daneUzytkownika(self):
        return DB.UserData(self.login)

    def edytujDane(self):
        rodzaj = input("Co chcesz edytowac?  ")
        wartosc = input("Nowa wartosc  ")
        cursor = connection.cursor()
        match rodzaj:
            case "email":
                self.email = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "email", wartosc, self.login))
            case "ulica":
                self.ulica = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "ulica", wartosc, self.login))
            case "lokal":
                self.lokal = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "lokal", wartosc, self.login))
            case "Kod pocztowy":
                self.kodPocztowy = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "kodPocztowy", wartosc, self.login))
            case "Nr telefonu":
                self.nrTel = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "nrTelefonu", wartosc, self.login))
        connection.commit()

    def wypiszDane(self):
        print(self.imie, self.nazwisko)
        print(self.miasto, self.ulica, self.lokal, self.kodPocztowy)
        print(self.email, self.nrTel)
