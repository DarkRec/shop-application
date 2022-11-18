class Produkt:
    def __init__(self, id: int, name, price: float, opis):
        self.id = id
        self.name = name
        self.price = price
        self.magazined = 0
        self.opis = opis
        #self.producent = producent

    def wyswietl(self):
        print(self.name, self.price, "zł\t", self.opis, self.magazined)

    def info(self):
        print(self.name, "%.2f" % round(self.price, 2))

    def zmienCene(self, newPrice: int):
        self.price = newPrice

    def dodaj(self, number: int):
        self.magazined += number

    def odejmij(self, number: int):
        if self.magazined - number < 0:
            print("Nie ma na tyle produktów, maksymalna liczba to", self.magazined)
        else:
            self.magazined -= number

    def stanMagazynu(self):
        print(self.magazined)
