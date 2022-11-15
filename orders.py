from datetime import date


class Zamowienie:
    def __init__(self, ProductList, value, status, date):
        self.ListaProduktow = ProductList
        self.wartosc = value
        self.status = status
        self.data = date

    def wypisz(self):
        print("======")
        print(f"wartosc - {self.wartosc} , status - {self.status}")
        print(f"data - {self.data}")

    def wyswietl(self):
        return (self.ListaProduktow, self.wartosc, self.status, self.data)


class Zamowienia:
    def __init__(self, ordersList, login):
        self.listaZamowien = ordersList
        self.login = login

    def wypiszZamowienia(self):
        for x in self.listaZamowien:
            zamowienie = x.wyswietl()
