#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produkt import Produkt


class ElementKoszyka:
    def __init__(self, produkt: str, ilosc: int | None = 1):
        self.produkt: Produkt = produkt
        self.ilosc: int = ilosc
        #self._unnamed_Koszyk_ : Koszyk = None
        """# @AssociationMultiplicity 1"""
        #self._unnamed_Zamowienie_ : Zamowienie = None
        """# @AssociationMultiplicity 1"""
        #self._unnamed_Produkt_ = []
        """# @AssociationMultiplicity 1..*"""
