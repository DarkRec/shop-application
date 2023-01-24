#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Zamowienie
from typing import List

from DB import *
from Produkt import Produkt
from ElementKoszyka import *


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

    def pokazZawartosc(self) -> ElementKoszyka:
        pass

    def dodaj(self) -> None:
        pass

    def usun(self) -> None:
        pass

    def zwieksz(self) -> None:
        pass

    def zmniejsz(self) -> None:
        pass

    def zmien(self, prod, ilosc) -> None:
        DB.EditCartProductNumber(prod, ilosc, self.login)
        self.obliczWartosc()

    def czyszczenie(self) -> None:
        pass

    def Tworzenie_Zamowienia(self) -> Zamowienie:
        pass

    def __init__(self, login):
        self.zawartosc: ElementKoszyka = []
        self.wartosc: int = 0
        self.login = login
        #self._unnamed_Klient_: Klient = None
        """# @AssociationMultiplicity 1"""

        """
            def __init__(self, login):
                    self.zawartosc = []
                    self.wartosc = 0
                    self.login = login
            """
