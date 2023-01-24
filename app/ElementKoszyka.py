#!/usr/bin/python
# -*- coding: UTF-8 -*-
from app.Produkt import Produkt


class ElementKoszyka:
    def __init__(self, produkt: str, ilosc: int | None = 1):
        self.produkt: Produkt = produkt
        self.ilosc: int = ilosc
