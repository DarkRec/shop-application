#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List
from DB import DB


class Zamowienie(object):
    def wyswietlZamowienie(self) -> None:
        pass

    def dodajZamowienie(self) -> None:
        DB.AddOrder(self.login, self.dane_Klienta, self.wartosc,
                    self.lista_Produktow, self.data_Utworzenia, self.status)

    def __init__(self, login: str, daneKlienta: str, value: float, productList: str, date, status: str):
        self.id: int = None
        self.login: str = login
        self.dane_Klienta: str = daneKlienta
        self.wartosc: float = value
        self.lista_Produktow: str = productList
        self.status: str = status
        self.data_Utworzenia: str = date  # date
        #self._unnamed_Zamowienia_: Zamowienia = None
        """# @AssociationMultiplicity 1"""
        #self._unnamed_ElementKoszyka_ = []
        """# @AssociationMultiplicity 1..*
			# @AssociationKind Aggregation"""
