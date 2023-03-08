#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from typing import List
from DB.DB import DB


class Zamowienie(object):

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
