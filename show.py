class Przegladanie:
    def __init__(self, produkty):
        self.listaProduktow = produkty
        self.strona = 1
        self.rozmiarStrony = 5

    def przegladanie(self):
        strona = []
        for x in range((self.strona-1)*self.rozmiarStrony, self.strona*self.rozmiarStrony):
            print(self.listaProduktow[x].name)
            strona.append(self.listaProduktow[x])
        return strona

    def wyswietl(self, nazwa):
        for produkt in self.listaProduktow:
            if produkt.name == nazwa:
                produkt.wyswietl()

    def wyszukaj(self, nazwa):
        wyszukane = []
        for produkt in self.listaProduktow:
            if nazwa.lower() in produkt.name:
                wyszukane.append(produkt)
        return wyszukane
