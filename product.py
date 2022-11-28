class Produkt:
    def __init__(self, id: int, name, price: float, ilosc, opis):
        self.id = id
        self.name = name
        self.price = price
        self.ilosc = ilosc
        self.opis = opis
        #self.producent = producent

    def wyswietl(self):
        print(self.name, self.price, "zł\t", self.opis, self.ilosc)

    def info(self):
        print(self.name, "%.2f" % round(self.price, 2))

    def zmienCene(self, newPrice: int):
        self.price = newPrice

    def dodaj(self, number: int):
        self.ilosc += number

    def odejmij(self, number: int):
        if self.ilosc - number < 0:
            print("Nie ma na tyle produktów, maksymalna liczba to", self.ilosc)
        else:
            self.ilosc -= number

    def stanMagazynu(self):
        print(self.ilosc)
