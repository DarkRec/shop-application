#!/usr/bin/python
# -*- coding: UTF-8 -*-
from app.Koszyk import Koszyk
from DB.DB import *


class Klient:
    def daneKlienta(self, login) -> str:
        return DB.UserData(login)

    def __init__(self, login):
        dane = self.daneKlienta(login)
        self.login: str = login
        self.imie: str = dane[1]
        self.nazwisko: str = dane[2]
        self.ulica: str = dane[3]
        self.nr_mieszkania: int = dane[4]
        self.kod_Pocztowy: str = dane[5]
        self.miasto: str = dane[6]
        self.email: str = dane[7]
        self.nr_Telefonu: str = dane[8]
        self.koszyk: Koszyk = Koszyk(login)
        self.type: str = 'client'
