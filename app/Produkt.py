#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from typing import List


class Produkt:
    def __init__(self, id: int, name, price: float, ilosc, opis: str, kategoria: str | None = 'brak'):
        self.id = id
        self.nazwa: str = name
        self.cena: float = price
        self.ilosc: int = ilosc
        self.opis: str = opis
        self.kategoria: str = kategoria
