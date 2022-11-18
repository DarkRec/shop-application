from connection import *
from cart import *


class Klient:
    def __init__(self, login, type) -> None:
        self.login = login
        self.koszyk = Koszyk(login)
        self.imie = self.daneOsobowe(login)[0]
        self.nazwisko = self.daneOsobowe(login)[1]
        self.email = self.daneKontaktowe(login)[0]
        self.nrTel = self.daneKontaktowe(login)[1]
        self.miasto = self.daneKontaktowe(login)[2]
        self.ulica = self.daneKontaktowe(login)[3]
        self.lokal = self.daneKontaktowe(login)[4]
        self.kodPocztowy = self.daneKontaktowe(login)[5]
        self.type = type
        self.wypiszDane()

    def daneOsobowe(self, login):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT imie, nazwisko FROM klienci WHERE username = '%s'" % (login))
        fetchedRow = cursor.fetchone()
        return fetchedRow

    def daneKontaktowe(self, login):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT email, nrTelefonu, miasto, ulica, lokal, kodPocztowy FROM klienci WHERE username = '%s'" % (login))
        fetchedRow = cursor.fetchone()
        return fetchedRow

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
