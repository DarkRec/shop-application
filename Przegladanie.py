#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from DB import DB as DB
from DB import *
from Produkt import Produkt
from typing import List


class Przegladanie:
    def loadFromDB(self) -> None:
        self.lista = []
        lista = DB.ProductsList()
        # print("lista")
        for row in lista:
            id = row[0]
            nazwa = row[1]
            cena = row[2]
            ilosc = row[3]
            try:
                opis = row[4]
            except:
                opis = ""
            self.lista.append(Produkt(id, nazwa, cena, ilosc, opis))

        # for x in self.lista:
            # x.wyswietl()

    def przegladanie(self) -> Produkt:
        self.loadFromDB()
        strona = []
        for x in range((self.strona-1)*self.rozmiarStrony, self.strona*self.rozmiarStrony):
            try:
                strona.append(self.lista[x])
            except:
                pass
        return strona

    def wystwietl(self) -> Produkt:
        pass

    def wyszukaj(self, nazwa: str) -> Produkt:
        self.strona = 1
        wyszukane = []
        for produkt in self.lista:
            if nazwa.lower() in produkt.nazwa.lower():
                wyszukane.append(produkt)
        return wyszukane

    def filtrowanie(self) -> Produkt:
        pass

    def __init__(self):
        self.lista: Produkt = []
        self.strona: int = 1
        self.rozmiarStrony: int = 8
        self._unnamed_Produkt_ = []
        self.loadFromDB()
        """# @AssociationMultiplicity 1..*
		# @AssociationKind Aggregation"""


Produkty = Przegladanie()
