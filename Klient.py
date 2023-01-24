#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Koszyk import Koszyk
from typing import List


class Klient:
    def edytujDane(self) -> None:
        pass

    def daneKlienta(self) -> str:
        pass

    def obliczanieRabatu(self):
        pass

    def __init__(self, dane):
        # (dane)
        self.login: str = dane[0]
        self.imie: str = dane[1]
        self.nazwisko: str = dane[2]
        self.ulica: str = dane[3]
        self.nr_mieszkania: int = dane[4]
        self.kod_Pocztowy: str = dane[5]
        self.miasto: str = dane[6]
        self.email: str = dane[7]
        self.nr_Telefonu: str = dane[8]
        self.type: str = 'client'
        self.koszyk: Koszyk = Koszyk(dane[0])
        #self.rabat: int = None
        #self._unnamed_Koszyk_: Koszyk = None
        """# @AssociationMultiplicity 1
		# @AssociationKind Composition"""
