from datetime import datetime
from connection import *
from tkinter import *
from guest import *
from index import *
from cart import *
from orders import *
from db import *
from show import *


class GUI:
    def __init__(self, window):
        self.window = window
        window.title("Internet Paper Shop Application")
        window.geometry('500x240')
        self.user = Gosc()
        self.PanelGoscia()

    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def PanelGoscia(self):  # ----- guest ----- #
        self.clear()
        Button(self.window,
               text="Lista Produktów",
               bg="blue",
               fg="yellow",
               command=lambda:self.ProductsList(1),
               width=15,
               ).grid(row=0, column=0, pady=10)
        Button(self.window,
               text="Logowanie",
               bg="blue",
               fg="yellow",
               width=15,
               command=self.PanelLogowania,  # lambda: PanelLogowania(user)
               ).grid(row=0, column=1)
        Button(self.window,
               text="Rejestracja",
               bg="blue",
               fg="yellow",
               width=15,
               command=self.PanelRejestracji,
               ).grid(row=0, column=2)

    def PanelLogowania(self):  # ----- login ----- #
        self.clear()

        def log_in():
            inputLogin = usernameEntry.get()
            inputPasswd = passwordEntry.get()
            self.user = Gosc.logowanie(inputLogin, inputPasswd)
            try:
                if self.user.type == 'user':
                    self.PanelKlienta()
            except:
                pass

        Label(self.window, text="login").grid(row=0, column=0)
        usernameEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        usernameEntry.grid(row=0, column=1)

        Label(self.window, text="hasło").grid(row=1, column=0)
        passwordEntry = Entry(self.window, fg="yellow",
                              bg="blue", width=20, show='*')
        passwordEntry.grid(row=1, column=1)

        Button(self.window,
               text="Logowanie",
               bg="blue",
               fg="yellow",
               command=log_in,
               ).grid(row=3, column=0, pady=10)

        Button(self.window,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.PanelGoscia,
               ).grid(row=3, column=1)

    def PanelRejestracji(self):  # ----- register ----- #
        self.clear()

        def register():
            login = usernameEntry.get()
            haslo = passwordEntry.get()
            imie = nameEntry.get()
            nazwisko = surnameEntry.get()
            email = emailEntry.get()
            miasto = cityEntry.get()
            ulica = streetEntry.get()
            lokal = houseEntry.get()
            kod = codeEntry.get()
            nrTel = telEntry.get()
            try:
                Gosc.rejestracja(login, haslo, imie, nazwisko,
                                 email, miasto, ulica, lokal, kod, nrTel)
            except:
                print("Błąd")
            else:
                self.user = Gosc.logowanie(login, haslo)
                if self.user.type == 'user':
                    self.PanelKlienta()

        Label(self.window, text="login").grid(row=1, column=0)
        usernameEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        usernameEntry.grid(row=1, column=1)

        Label(self.window, text="hasło").grid(row=1, column=2)
        passwordEntry = Entry(self.window, fg="yellow",
                              bg="blue", width=20, show='*')
        passwordEntry.grid(row=1, column=3, pady=10)

        Label(self.window, text="imie").grid(row=2, column=0)
        nameEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        nameEntry.grid(row=2, column=1)

        Label(self.window, text="nazwisko").grid(row=2, column=2)
        surnameEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        surnameEntry.grid(row=2, column=3)

        Label(self.window, text="ulica").grid(row=3, column=0)
        streetEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        streetEntry.grid(row=3, column=1)

        Label(self.window, text="nr mieszkania").grid(row=3, column=2)
        houseEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        houseEntry.grid(row=3, column=3)

        Label(self.window, text="kod pocztowy").grid(row=4, column=0)
        codeEntry = Entry(self.window, fg="yellow", bg="blue", width=6)
        codeEntry.grid(row=4, column=1)

        Label(self.window, text="miasto").grid(row=4, column=2)
        cityEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        cityEntry.grid(row=4, column=3)

        Label(self.window, text="e-mail").grid(row=5, column=0)
        emailEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        emailEntry.grid(row=5, column=1)

        Label(self.window, text="nr telefonu").grid(row=5, column=2)
        telEntry = Entry(self.window, fg="yellow", bg="blue", width=12)
        telEntry.grid(row=5, column=3)

        Button(self.window,
               text="Rejestracja",
               bg="blue",
               fg="yellow",
               command=register,
               ).grid(row=7, column=1, pady=10)

        Button(self.window,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.PanelGoscia,
               ).grid(row=7, column=2)

    def PanelKlienta(self):  # ----- client panel ----- #
        self.clear()
        # Label(self.window, text="Użytkownik:%s" %
        #      (self.user.login)).grid(row=0, column=0)

        Button(self.window,
               text="Lista Produktów",
               bg="blue",
               fg="yellow",
               command=lambda:self.ProductsList(1),
               width=15,
               ).grid(row=0, column=0, pady=10)

        Button(self.window,
               text=f"{self.user.login}",
               bg="blue",
               fg="yellow",
               command=self.Account,
               width=15,
               ).grid(row=0, column=1)

        Button(self.window,
               text="Koszyk",
               bg="blue",
               fg="yellow",
               command=self.CartList,
               width=15,
               ).grid(row=0, column=2)
               

# ----- products list ----- #

    def ProductsList(self, strona):
        Produkty.strona = strona
        self.clear()
        try:
            if self.user.type == "user":
                self.PanelKlienta()
        except:
            self.PanelGoscia()
        x = 2

        def Add(prod, username):
            DB.AddToCart(prod, username)
            self.ProductsList(Produkty.strona)

        def Remove(prod, username):
            DB.RemoveFromCart(prod, username)
            self.ProductsList(Produkty.strona)

        Label(self.window, text="Wyszukaj: ").grid(row=1, column=0)
        searchInput = Entry(self.window, width=8)
        searchInput.grid(row=1, column=1)

        Button(self.window,
               text="Search",
               bg="blue",
               fg="yellow",
               command=lambda:self.Search(Produkty.wyszukaj(searchInput.get())),
               width=15,
               ).grid(row=1, column=2)

        for prod in Produkty.przegladanie(Produkty.lista):   # in range(Produkty.rozmiarStrony)
            try:
                Label(self.window, text=f"{prod.name}", height=1).grid(
                    row=x, column=0)
                Label(self.window, text="%.2fzł" % round(prod.price, 2)).grid(
                    row=x, column=1)
            except:
                pass

            try:
                if self.user.type == 'user':
                    if (DB.ProdInCart(prod.name) == 0):
                        Button(self.window, text="Dodaj do koszyka", command=lambda tempName=prod.name: Add(
                            tempName, self.user.login)).grid(row=x, column=2)
                    else:
                        Button(self.window, text="Usuń z koszyka", command=lambda tempName=prod.name: Remove(
                            tempName, self.user.login)).grid(row=x, column=2)
            except:
                pass
            x += 1
        while x < Produkty.rozmiarStrony+2:
            Label(self.window, text=" ", height=1).grid(row=x, column=0)
            x+=1

        def Prev():
            Produkty.strona -= 1
            if Produkty.strona == 0:
                Produkty.strona = 1
            self.ProductsList(Produkty.strona)

        def Next():
            Produkty.strona += 1
            self.ProductsList(Produkty.strona)

        Button(self.window,
               text="<",
               bg="blue",
               fg="yellow",
               command=Prev,
               width=5,
               ).grid(row=x, column=1, sticky=W, pady=10)

        Button(self.window,
               text=">",
               bg="blue",
               fg="yellow",
               command=Next,
               width=5,
               ).grid(row=x, column=1, sticky=E, pady=10)

    def Search(self, searchResults):
            self.clear()
            try:
                if self.user.type == "user":
                    self.PanelKlienta()
            except:
                self.PanelGoscia()

            Button(self.window,
                   text="X",
                   bg="blue",
                   fg="yellow",
                   width=15,
                   command=lambda:self.ProductsList(1),
                   ).grid(row=1, column=2)
            Label(self.window, text=" ", height=1).grid(row=1, column=0)
            b = 2
            for x in searchResults:
                Label(self.window, text=f"{x.name}", height=1).grid(row=b, column=0)
                Label(self.window, text="%.2fzł" %
                      round(x.price, 2)).grid(row=b, column=1)
                b += 1


            def Prev(searchResults):
                Produkty.strona -= 1
                if Produkty.strona == 0:
                    Produkty.strona = 1
                self.Search(searchResults)

            def Next(searchResults):
                Produkty.strona += 1
                self.Search(searchResults)

            Button(self.window,
                    text="<",
                    bg="blue",
                    fg="yellow",
                    command=lambda:Prev(searchResults),
                    width=5,
                    ).grid(row=b, column=1, sticky=W, pady=10)

            Button(self.window,
                    text=">",
                    bg="blue",
                    fg="yellow",
                    command=lambda:Next(searchResults),
                    width=5,
                    ).grid(row=b, column=1, sticky=E, pady=10)

# ----- account ----- #

    def Account(self):
        self.clear
        self.PanelKlienta()

        Button(self.window,
               text="Dane",
               bg="blue",
               fg="yellow",
               command=self.AccountData,
               width=15,
               ).grid(row=2, column=0)

        Button(self.window,
               text="Zamowienia",
               bg="blue",
               fg="yellow",
               command=self.OrdersList,
               width=15,
               ).grid(row=2, column=1)

    def AccountData(self):
        self.clear
        self.PanelKlienta()

        self.user.wypiszDane()

        Label(self.window,
              text=f"Imie: {self.user.daneOsobowe(self.user.login)[0]}"
              ).grid(row=3, column=0)  # .grid(row=x, column=0)

        Label(self.window,
              text=f"Nazwisko: {self.user.daneOsobowe(self.user.login)[1]}"
              ).grid(row=3, column=1)

        Label(self.window,
              text=f"Ulica: {self.user.daneKontaktowe(self.user.login)[3]}"
              ).grid(row=4, column=0)

        Label(self.window,
              text=f"Nr mieszkania: {self.user.daneKontaktowe(self.user.login)[4]}"
              ).grid(row=4, column=1)

        Label(self.window,
              text=f"Kod Pocztowy: {self.user.daneKontaktowe(self.user.login)[5]}"
              ).grid(row=5, column=0)

        Label(self.window,
              text=f"Miasto: {self.user.daneKontaktowe(self.user.login)[2]}"
              ).grid(row=5, column=1)

        Label(self.window,
              text=f"Email: {self.user.daneKontaktowe(self.user.login)[0]}"
              ).grid(row=6, column=0)

        Label(self.window,
              text=f"Nr Telefonu: {self.user.daneKontaktowe(self.user.login)[1]}"
              ).grid(row=6, column=1)


# ----- cart ----- #

    def CartList(self):
        self.clear
        self.PanelKlienta()
        cartUpdate = []
        x = 2
        self.user.koszyk.loadFromDB()
        for prod in self.user.koszyk.zawartosc:
            cartName = Label(self.window,
                             text=f"{prod.produkt.name}")  # .grid(row=x, column=0)
            cartName.grid(row=x, column=0)

            cartPrice = Label(self.window,
                              text="%.2fzł" % round(prod.produkt.price, 2))  # .grid(row=x, column=0)
            cartPrice.grid(row=x, column=1)

            cartNumber = Entry(self.window, width=8)
            cartNumber.insert(0, f"{prod.ilosc}")
            cartNumber.grid(row=x, column=2)
            cartUpdate.append((cartName, cartNumber))


            def Remove(prod, username):
                DB.RemoveFromCart(prod, username)
                self.CartList()

            Button(self.window, text="X", bg="red",command=lambda tempName=prod.produkt.name: Remove(
                    tempName, self.user.login)).grid(row=x, column=3)
                    
            x += 1

        endPrice = Label(self.window,
                         text=f"Suma: {self.user.koszyk.obliczWartosc()}")  # .grid(row=x, column=0)
        endPrice.grid(row=x, column=2)

        Button(self.window,
               text="Zapisz",
               bg="blue",
               fg="yellow",
               command=lambda: self.CartEdit(cartUpdate),
               width=6,
               ).grid(row=x+1, column=2, sticky=W)

        Button(self.window,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.CartList,
               width=6,
               ).grid(row=x+1, column=2, sticky=E)

        Button(self.window,
               text="Złóż zamówiene",
               bg="blue",
               fg="yellow",
               command=lambda: self.OrderData(self.user),
               width=15,
               ).grid(row=x+2, column=2, pady=5)

    def CartEdit(self, update):
        global cart
        for x in update:
            self.user.koszyk.zmien(x[0]['text'], x[1].get())
        self.CartList()

# ----- orders ----- #

    def OrdersList(self):
        self.clear
        self.PanelKlienta()
        Label(self.window, text="cena").grid(row=2, column=0)
        Label(self.window, text="data zamówienia").grid(row=2, column=1)
        Label(self.window, text="status").grid(row=2, column=2)
        b=3
        orders = Zamowienia(DB.loadOrders(self.user.login), self.user.login)
        for x in orders.lista:
            Label(self.window, text=f"{x[0]}").grid(row=b, column=0)
            Label(self.window, text=f"{x[1]}").grid(row=b, column=1)
            Label(self.window, text=f"{x[2]}").grid(row=b, column=2)
            b+=1
            print(x[0],x[1],x[2])
            #"%.2fzł" % round(prod.produkt.price, 2)

    def OrderData(self, klient):
        # klient.koszyk.loadFromDB()
        # klient.koszyk.obliczWartosc()
        # now = date.today()
        # now.strftime('%Y-%m-%d %H:%M:%S')
        # order = Zamowienie(klient.login, klient.koszyk.wartosc, klient.koszyk.zawartosc, now, 'waiting for authorization')
        self.clear()

        def createOrder(klient):
            imie = nameEntry.get()
            nazwisko = surnameEntry.get()
            email = emailEntry.get()
            miasto = cityEntry.get()
            ulica = streetEntry.get()
            lokal = houseEntry.get()
            kod = codeEntry.get()
            nrTel = telEntry.get()

            DB.UpdateClient(klient.login, imie, nazwisko, email, nrTel,miasto, ulica, lokal, kod)

            klient.koszyk.loadFromDB()
            klient.koszyk.obliczWartosc()
            now = datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            daneKlienta = (imie, nazwisko, email,
                           nrTel, miasto, ulica, lokal, kod)
            order = Zamowienie(klient.login, ''.join(f"{str(e)};" for e in daneKlienta), klient.koszyk.wartosc,
                               ''.join(f"{str(e.produkt.id)}-{str(e.ilosc)};" for e in klient.koszyk.zawartosc), now, 'waiting for authorization')
            order.dodajZamowienie()
            cursor = connection.cursor()
            DB.FromCartToOrder(klient.koszyk.zawartosc,klient.login)
            klient.koszyk.wartosc = 0
            self.PanelKlienta()

        Label(self.window, text="imie").grid(row=2, column=0)
        nameEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        nameEntry.grid(row=2, column=1)
        nameEntry.insert(0, f"{klient.imie}")

        Label(self.window, text="nazwisko").grid(row=2, column=2)
        surnameEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        surnameEntry.grid(row=2, column=3)
        surnameEntry.insert(0, f"{klient.nazwisko}")

        Label(self.window, text="ulica").grid(row=3, column=0)
        streetEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        streetEntry.grid(row=3, column=1)
        streetEntry.insert(0, f"{klient.ulica}")

        Label(self.window, text="nr mieszkania").grid(row=3, column=2)
        houseEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        houseEntry.grid(row=3, column=3)
        houseEntry.insert(0, f"{klient.lokal}")

        Label(self.window, text="kod pocztowy").grid(row=4, column=0)
        codeEntry = Entry(self.window, fg="yellow", bg="blue", width=6)
        codeEntry.grid(row=4, column=1)
        codeEntry.insert(0, f"{klient.kodPocztowy}")

        Label(self.window, text="miasto").grid(row=4, column=2)
        cityEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        cityEntry.grid(row=4, column=3)
        cityEntry.insert(0, f"{klient.miasto}")

        Label(self.window, text="e-mail").grid(row=5, column=0)
        emailEntry = Entry(self.window, fg="yellow", bg="blue", width=20)
        emailEntry.grid(row=5, column=1)
        emailEntry.insert(0, f"{klient.email}")

        Label(self.window, text="nr telefonu").grid(row=5, column=2)
        telEntry = Entry(self.window, fg="yellow", bg="blue", width=12)
        telEntry.grid(row=5, column=3)
        telEntry.insert(0, f"{klient.nrTel}")

        Button(self.window,
               text="Zakończ",
               bg="blue",
               fg="yellow",
               command=lambda: createOrder(self.user),
               ).grid(row=7, column=1, pady=10)

        Button(self.window,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.CartList,
               ).grid(row=7, column=2)


root = Tk()
gui = GUI(root)
root.mainloop()
