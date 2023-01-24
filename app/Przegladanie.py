#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app.DB import *
from app.Produkt import Produkt


class Przegladanie:
    def loadFromDB(self) -> None:
        self.lista = []
        lista = DB.ProductsList()
        for row in lista:
            id = row[0]
            nazwa = row[1]
            cena = row[2]
            ilosc = row[3]
            try:
                opis = row[4]
            except:
                opis = ""
            kategoria = row[5]
            self.lista.append(Produkt(id, nazwa, cena, ilosc, opis, kategoria))

    def przegladanie(self) -> Produkt:
        self.loadFromDB()
        strona = []
        for x in range((self.strona-1)*self.rozmiarStrony, self.strona*self.rozmiarStrony):
            try:
                strona.append(self.lista[x])
            except:
                pass
        return strona

    def wystwietl(self, id) -> Produkt:
        for x in self.lista:
            if x.id == id:
                return x

    def wyszukaj(self, nazwa: str) -> Produkt:
        self.strona = 1
        wyszukane = []
        for produkt in self.lista:
            if nazwa.lower() in produkt.nazwa.lower():
                wyszukane.append(produkt)
        return wyszukane

    def filtruj(self, nazwa: str) -> Produkt:
        self.strona = 1
        wyszukane = []
        for produkt in self.lista:
            if nazwa == produkt.kategoria:
                wyszukane.append(produkt)
        return wyszukane

    def __init__(self):
        self.lista: Produkt = []
        self.strona: int = 1
        self.rozmiarStrony: int = 8
        self.loadFromDB()


Produkty = Przegladanie()
