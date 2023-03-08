#!/usr/bin/python
# -*- coding: UTF-8 -*-
from app.Zamowienie import *

from DB.DB import *
from app.Produkt import Produkt
from app.ElementKoszyka import *


class Koszyk:
    def loadFromDB(self) -> None:
        self.zawartosc = []
        for row in DB.ClientCart(self.login):
            self.zawartosc.append(ElementKoszyka(
                Produkt(row[0], row[1], row[2], row[3], row[4], row[5]), row[6]))

    def obliczWartosc(self) -> float:
        self.wartosc = 0
        for el in self.zawartosc:
            self.wartosc += (el.produkt.cena * el.ilosc)
        return "%.2fzł" % round(self.wartosc, 2)

    def zmien(self, prod, ilosc) -> None:
        DB.EditCartProductNumber(prod, ilosc, self.login)
        self.obliczWartosc()

    def __init__(self, login):
        self.zawartosc: ElementKoszyka = []
        self.wartosc: float = 0
        self.login: str = login
