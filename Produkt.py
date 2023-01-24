#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List


class Produkt:
    def __init__(self, id: int, name, price: float, ilosc, opis: str, kategoria: str | None = 'brak'):
        self.id = id
        self.nazwa: str = name
        self.cena: float = price
        self.ilosc: int = ilosc
        self.opis: str = opis
        #self.zdjecie: str = None
        self.kategorie: str = kategoria
        #self._unnamed_Przegladanie_: Przegladanie = None
        """# @AssociationMultiplicity 1"""
        #self._unnamed_ElementKoszyka_ = []
        """# @AssociationMultiplicity 1..*"""

    def wyswietl(self) -> None:
        print(self.nazwa, self.cena, "zł\t",
              self.opis, self.ilosc)
