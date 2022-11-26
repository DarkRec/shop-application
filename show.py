from connection import *
from product import *


class Przegladanie:
    def __init__(self):
        self.lista = []

        self.loadFromDB()
        self.strona = 1
        self.rozmiarStrony = 5

    def loadFromDB(self):
        cursor = connection.cursor()
        cursor.execute("SELECT _id, nazwa, cena FROM Produkty")
        fetchedRows = cursor.fetchall()

        for row in fetchedRows:
            id = row[0]
            nazwa = row[1]
            cena = row[2]
            try:
                opis = row[3]

            except:
                opis = ""
            self.lista.append(Produkt(id, nazwa, cena, opis))

    def przegladanie(self, lista):
        strona = []
        for x in range((self.strona-1)*self.rozmiarStrony, self.strona*self.rozmiarStrony):
            try:
                strona.append(lista[x])
            except:
                pass
        return strona

    def wyswietl(self, nazwa):
        for produkt in self.lista:
            if produkt.name == nazwa:
                produkt.wyswietl()

    def wyszukaj(self, nazwa):
        self.strona = 1
        wyszukane = []
        for produkt in self.lista:
            if nazwa.lower() in produkt.name:
                wyszukane.append(produkt)
        return wyszukane


Produkty = Przegladanie()
