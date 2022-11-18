from connection import *
from product import *
from db import *


class ElementKoszyka:
    def __init__(self, produkt, ilosc):
        self.produkt = produkt
        self.ilosc = ilosc


class Koszyk:
    def __init__(self, login):
        self.zawartosc = []
        self.wartosc = 0
        self.login = login

    def loadFromDB(self):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT produkty._id, produkt, cena, opis, koszyk.ilosc FROM koszyk INNER JOIN produkty ON koszyk.produkt = produkty.nazwa WHERE username = '%s';" % (self.login))
        fetchedRows = cursor.fetchall()

        self.zawartosc = []
        for row in fetchedRows:
            self.zawartosc.append(ElementKoszyka(
                Produkt(row[0], row[1], row[2], row[3]), row[4]))

    def obliczWartosc(self):
        self.wartosc = 0
        for el in self.zawartosc:
            self.wartosc += (el.produkt.price * el.ilosc)
        return "%.2fzł" % round(self.wartosc, 2)
        # print(self.wartosc)

    def pokazZawartosc(self):
        for el in self.zawartosc:
            # el.produkt.info()
            print(el.produkt.name, "%.2fzł" %
                  round(el.produkt.price, 2), "-", el.ilosc, "szt")
        return self.zawartosc

    def dodaj(self, produkt, ilosc):
        self.loadFromDB()
        for el in self.zawartosc:
            if produkt.name == el.produkt.name:
                if ilosc > 0:
                    self.zwieksz(el, ilosc)
                return 0
        if ilosc > 0:
            self.zawartosc.append(ElementKoszyka(produkt, ilosc))
        self.obliczWartosc()
        # cursor = connection.cursor()
        # cursor.execute(
        #    "INSERT INTO users (`username`, `password`) VALUES ('%s', '%s');" % (login, haslo))
        # connection.commit()

    def usun(self, produkt):
        for el in self.zawartosc:
            if produkt.name == el.produkt.name:
                self.zawartosc.remove(el)
        self.obliczWartosc()

    def zwieksz(self, prod, ilosc):
        if (ilosc > 0):
            prod.ilosc += ilosc
            connection.cursor().execute("UPDATE `koszyk` SET `ilosc` = '%i' WHERE (`username` = '%s' AND `produkt` = '%s');" %
                                        (prod.ilosc, self.login, prod.produkt.name))
            connection.commit()
            self.obliczWartosc()

    def zmniejsz(self, prod, ilosc):
        if (ilosc > 0):
            for el in self.zawartosc:
                if prod.name == el.produkt.name:
                    el.ilosc -= ilosc
                    if el.ilosc < 1:
                        el.ilosc = 1
                    connection.cursor().execute("UPDATE `koszyk` SET `ilosc` = '%i' WHERE (`username` = '%s' AND `produkt` = '%s');" %
                                                (el.ilosc, self.login, el.produkt.name))
                    connection.commit()
                    self.obliczWartosc()

    def zmien(self, prod, ilosc):
        DB.editCartProdNum(prod, ilosc, self.login)
        self.obliczWartosc()

    def czyszczenie(self):
        self.zawartosc = []
        self.wartosc = 0
