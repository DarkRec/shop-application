from datetime import date
from connection import *
from db import *


class Zamowienie:
    def __init__(self, login, daneKlienta, value, productList, date, status):
        self.login = login
        self.klient = daneKlienta
        self.wartosc = value
        self.listaProduktow = productList
        self.data = date
        self.status = status

    def wypisz(self):
        print("======")
        print(f"wartosc - {self.wartosc} , status - {self.status}")
        print(f"data - {self.data}")

    def wyswietl(self):
        return (self.listaProduktow, self.wartosc, self.status, self.data)

    def dodajZamowienie(self):
        DB.AddOrder(self.login, self.klient, self.wartosc,
                    self.listaProduktow, self.data)


class Zamowienia:
    def __init__(self, ordersList, login):
        self.lista = ordersList
        self.login = login

    def wypiszZamowienia(self):
        for x in self.listaZamowien:
            zamowienie = x.wyswietl()
