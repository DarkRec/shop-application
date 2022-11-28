from datetime import datetime
from tkinter import *
from tkinter import scrolledtext
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
        window.geometry('800x400')  # '250x200+250+200'
        window.option_add('*tearOff', FALSE)
        self.main = Frame(window)
        # self.main.pack(padx=0, pady=10)
        self.main.place(x=5, y=0)
        self.user = Gosc()
        self.PanelGoscia()
        self.ProductsList(1)

    def delete(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def ClearGUI(self):
        for widget in self.main.winfo_children():
            widget.destroy()
            # if type(label) == Label:  # just Label since you used a wildcard import to import tkinter
            #    label.destroy()

# --------------- guest --------------- #

    def PanelGoscia(self):  # ----- guest panel ----- #
        self.ClearGUI()

        menubar = Menu(self.window)
        menubar.add_cascade(label="Lista Produktów",
                            command=lambda: self.ProductsList(1))

        menubar.add_separator()

        menubar.add_cascade(label="Logowanie",
                            command=self.PanelLogowania)

        menubar.add_separator()

        menubar.add_cascade(label="Rejestracja",
                            command=self.PanelRejestracji)

        self.window['menu'] = menubar

    def PanelLogowania(self):  # ----- login ----- #
        self.ClearGUI()

        def log_in():
            inputLogin = usernameEntry.get()
            inputPasswd = passwordEntry.get()
            self.user = Gosc.logowanie(inputLogin, inputPasswd)
            try:
                if self.user.type == 'user':
                    self.PanelKlienta()
                elif self.user.type == "admin":
                    self.PanelAdmina()
            except:
                print("Błąd Logowania")
            finally:
                self.ClearGUI()
        Label(self.main, text="login").grid(row=0, column=0)
        usernameEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        usernameEntry.grid(row=0, column=1)

        Label(self.main, text="hasło").grid(row=1, column=0)
        passwordEntry = Entry(self.main, fg="yellow",
                              bg="blue", width=20, show='*')
        passwordEntry.grid(row=1, column=1)

        Button(self.main,
               text="Logowanie",
               bg="blue",
               fg="yellow",
               command=log_in,
               ).grid(row=3, column=0, pady=10)

        Button(self.main,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.PanelGoscia,
               ).grid(row=3, column=1)

    def PanelRejestracji(self):  # ----- register ----- #
        self.ClearGUI()

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
            finally:
                self.user = Gosc.logowanie(login, haslo)
                # if self.user.type == 'user':
                #    self.PanelKlienta()
                # elif self.user.tpye == "admin":
                #    self.PanelAdmina()

        Label(self.main, text="login").grid(row=1, column=0)
        usernameEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        usernameEntry.grid(row=1, column=1)

        Label(self.main, text="hasło").grid(row=1, column=2)
        passwordEntry = Entry(self.main, fg="yellow",
                              bg="blue", width=20, show='*')
        passwordEntry.grid(row=1, column=3)

        Label(self.main, text="imie").grid(row=2, column=0)
        nameEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        nameEntry.grid(row=2, column=1)

        Label(self.main, text="nazwisko").grid(row=2, column=2)
        surnameEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        surnameEntry.grid(row=2, column=3)

        Label(self.main, text="ulica").grid(row=3, column=0)
        streetEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        streetEntry.grid(row=3, column=1)

        Label(self.main, text="nr mieszkania").grid(row=3, column=2)
        houseEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        houseEntry.grid(row=3, column=3)

        Label(self.main, text="kod pocztowy").grid(row=4, column=0)
        codeEntry = Entry(self.main, fg="yellow", bg="blue", width=6)
        codeEntry.grid(row=4, column=1)

        Label(self.main, text="miasto").grid(row=4, column=2)
        cityEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        cityEntry.grid(row=4, column=3)

        Label(self.main, text="e-mail").grid(row=5, column=0)
        emailEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        emailEntry.grid(row=5, column=1)

        Label(self.main, text="nr telefonu").grid(row=5, column=2)
        telEntry = Entry(self.main, fg="yellow", bg="blue", width=12)
        telEntry.grid(row=5, column=3)

        Button(self.main,
               text="Rejestracja",
               bg="blue",
               fg="yellow",
               command=register,
               ).grid(row=7, column=1, pady=10)

        Button(self.main,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.PanelGoscia,
               ).grid(row=7, column=2)

# --------------- client --------------- #

    def Wylogowywanie(self):
        self.user = Gosc()
        self.PanelGoscia()

    def PanelKlienta(self):  # ----- client panel ----- #
        # self.ClearGUI()
        menubar = Menu(self.window)
        menubar.add_cascade(label="Lista Produktów",
                            command=lambda: self.ProductsList(1))
        menubar.add_separator()

        menubar.add_cascade(label=f"{self.user.login}",
                            command=self.Account)
        menubar.add_separator()

        menubar.add_cascade(label="Koszyk",
                            command=self.CartList)
        menubar.add_separator()

        menubar.add_cascade(label="Wyloguj",
                            command=self.Wylogowywanie)

        self.window['menu'] = menubar

# ----- products list ----- #

    def ProductsList(self, strona):
        Produkty.strona = strona
        self.ClearGUI()

        x = 2

        def AddToCart(prod, username):
            DB.AddToCart(prod, username)
            self.ProductsList(Produkty.strona)

        def RemoveFromCart(prod, username):
            DB.RemoveFromCart(prod, username)
            self.ProductsList(Produkty.strona)

        def RemoveProduct(prod, id):
            DB.RemoveProduct(prod, id)
            for x, i in enumerate(Produkty.lista):
                if i.name == prod:
                    del Produkty.lista[x]
            self.ProductsList(Produkty.strona)

        Label(self.main, text="Wyszukaj: ").grid(row=1, column=0, padx=25)
        searchInput = Entry(self.main, width=10)
        searchInput.grid(row=1, column=1, padx=25)

        Button(self.main,
               text="Search",
               bg="blue",
               fg="yellow",
               command=lambda: self.Search(
                   Produkty.wyszukaj(searchInput.get())),
               width=15).grid(row=1, column=2, padx=25)

        # in range(Produkty.rozmiarStrony)
        for prod in Produkty.przegladanie(Produkty.lista):
            try:
                Label(self.main, text=f"{prod.name}", height=1).grid(
                    row=x, column=0)
                Label(self.main, text="%.2fzł" % round(prod.price, 2)).grid(
                    row=x, column=1)
                Button(self.main, text="Info", bg="blue", command=lambda tempname=prod.name: self.ProductInfo(
                    tempname)).grid(row=x, column=2)
            except:
                pass

            try:
                if self.user.type == 'user':
                    if (DB.ProdInCart(prod.name) == 0):
                        Button(self.main, text="Dodaj do koszyka", bg="green", command=lambda tempname=prod.name: AddToCart(
                            tempname, self.user.login)).grid(row=x, column=2)
                    else:
                        Button(self.main, text="Usuń z koszyka", bg="red", command=lambda tempname=prod.name: RemoveFromCart(
                            tempname, self.user.login)).grid(row=x, column=2)
                if self.user.type == 'admin':
                    # print(prod.name)
                    Button(self.main, text="Usuń produkt", bg="red",
                           command=lambda tempID=prod.id, tempname=prod.name: RemoveProduct(tempID, tempname)).grid(row=x, column=2)
            except:
                pass
            x += 1
        while x < Produkty.rozmiarStrony+2:
            Label(self.main, text=" ", height=1).grid(row=x, column=0)
            x += 1

        def Prev():
            Produkty.strona -= 1
            if Produkty.strona == 0:
                Produkty.strona = 1
            try:
                if self.user.type == "user":
                    self.ProductsList(Produkty.strona)
                elif self.user.type == "admin":
                    self.EditProduct(Produkty.strona)
            except:
                self.ProductsList(Produkty.strona)

        def Next():
            Produkty.strona += 1
            try:
                if self.user.type == "user":
                    self.ProductsList(Produkty.strona)
                elif self.user.type == "admin":
                    self.EditProduct(Produkty.strona)
            except:
                self.ProductsList(Produkty.strona)

        Button(self.main,
               text="<",
               bg="blue",
               fg="yellow",
               command=Prev,
               width=5,
               ).grid(row=x, column=1, sticky=W, pady=10)

        Button(self.main,
               text=">",
               bg="blue",
               fg="yellow",
               command=Next,
               width=5,
               ).grid(row=x, column=1, sticky=E, pady=10)

    def ProductInfo(self, nazwa):
        self.ClearGUI()
        for x in Produkty.lista:
            if x.name == nazwa:
                Label(self.main, text=f"{x.name}", font=(
                    "Arial", 25)).grid(row=0, column=0, padx=5)

                frm = Frame(self.main, width=300, height=200)
                frm.grid(row=1, column=0, padx=5)

                Label(frm, text=f"{x.price}").grid(
                    row=0, column=0, padx=5)

                #Label(frm, text=f"{x.ilosc}").grid(row=0, column=1, padx=5)

                Label(self.main, text=f"{x.opis}").grid(
                    row=2, column=0, padx=5)
                Button(self.main,
                       text="Cofnij",
                       bg="blue",
                       fg="yellow",
                       width=15,
                       command=lambda: self.ProductsList(Produkty.strona),
                       ).grid(row=3, column=0)
                break

    def Search(self, searchResults):
        self.ClearGUI()
        try:
            if self.user.type == "user":
                self.PanelKlienta()
        except:
            self.PanelGoscia()

        Button(self.main,
               text="X",
               bg="blue",
               fg="yellow",
               width=15,
               command=lambda: self.ProductsList(1),
               ).grid(row=1, column=2)
        Label(self.main, text=" ", height=1).grid(row=1, column=0)

        b = 2
        for x in searchResults:
            Label(self.main, text=f"{x.name}",
                  height=1, width=10).grid(row=b, column=0, padx=25)
            Label(self.main, text="%.2fzł" %
                  round(x.price, 2)).grid(row=b, column=1, padx=25)
            b += 1

        def Prev(searchResults):
            Produkty.strona -= 1
            if Produkty.strona == 0:
                Produkty.strona = 1
            self.Search(searchResults)

        def Next(searchResults):
            Produkty.strona += 1
            self.Search(searchResults)

        Button(self.main,
               text="<",
               bg="blue",
               fg="yellow",
               command=lambda: Prev(searchResults),
               width=5,
               ).grid(row=b, column=1, sticky=W, pady=10)

        Button(self.main,
               text=">",
               bg="blue",
               fg="yellow",
               command=lambda: Next(searchResults),
               width=5,
               ).grid(row=b, column=1, sticky=E, pady=10)

# ----- account ----- #

    def Account(self):
        self.ClearGUI()
        # self.PanelKlienta()

        Button(self.main,
               text="Dane",
               bg="blue",
               fg="yellow",
               command=self.AccountData,
               width=15,
               ).grid(row=2, column=0)

        Button(self.main,
               text="Zamowienia",
               bg="blue",
               fg="yellow",
               command=self.OrdersList,
               width=15,
               ).grid(row=2, column=1)

    def AccountData(self):
        self.ClearGUI()
        # self.PanelKlienta()

        self.user.wypiszDane()

        Label(self.main,
              text=f"Imie: {self.user.daneUzytkownika()[0]}"
              ).grid(row=3, column=0)  # .grid(row=x, column=0)

        Label(self.main,
              text=f"Nazwisko: {self.user.daneUzytkownika()[1]}"
              ).grid(row=3, column=1)

        Label(self.main,
              text=f"Ulica: {self.user.daneUzytkownika()[5]}"
              ).grid(row=4, column=0)

        Label(self.main,
              text=f"Nr mieszkania: {self.user.daneUzytkownika()[6]}"
              ).grid(row=4, column=1)

        Label(self.main,
              text=f"Kod Pocztowy: {self.user.daneUzytkownika()[7]}"
              ).grid(row=5, column=0)

        Label(self.main,
              text=f"Miasto: {self.user.daneUzytkownika()[4]}"
              ).grid(row=5, column=1)

        Label(self.main,
              text=f"Email: {self.user.daneUzytkownika()[2]}"
              ).grid(row=6, column=0)

        Label(self.main,
              text=f"Nr Telefonu: {self.user.daneUzytkownika()[3]}"
              ).grid(row=6, column=1)


# ----- cart ----- #


    def CartList(self):
        self.ClearGUI()
        # self.PanelKlienta()
        cartUpdate = []
        x = 2
        self.user.koszyk.loadFromDB()
        for prod in self.user.koszyk.zawartosc:
            cartName = Label(self.main,
                             text=f"{prod.produkt.name}")  # .grid(row=x, column=0)
            cartName.grid(row=x, column=0)

            cartPrice = Label(self.main,
                              text="%.2fzł" % round(prod.produkt.price, 2))  # .grid(row=x, column=0)
            cartPrice.grid(row=x, column=1)

            cartNumber = Entry(self.main, width=8)
            cartNumber.insert(0, f"{prod.ilosc}")
            cartNumber.grid(row=x, column=2)
            cartUpdate.append((cartName, cartNumber))

            def Remove(prod, username):
                DB.RemoveFromCart(prod, username)
                self.CartList()

            Button(self.main, text="X", bg="red", command=lambda tempname=prod.produkt.name: Remove(
                tempname, self.user.login)).grid(row=x, column=3)

            x += 1

        endPrice = Label(self.main,
                         text=f"Suma: {self.user.koszyk.obliczWartosc()}")  # .grid(row=x, column=0)
        endPrice.grid(row=x, column=2)

        Button(self.main,
               text="Zapisz",
               bg="blue",
               fg="yellow",
               command=lambda: self.CartEdit(cartUpdate),
               width=6,
               ).grid(row=x+1, column=2, sticky=W)

        Button(self.main,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.CartList,
               width=6,
               ).grid(row=x+1, column=2, sticky=E)

        Button(self.main,
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
        self.ClearGUI()
        # self.PanelKlienta()
        Label(self.main, text="cena").grid(row=2, column=0)
        Label(self.main, text="data zamówienia").grid(row=2, column=1)
        Label(self.main, text="status").grid(row=2, column=2)
        b = 3
        orders = Zamowienia(DB.loadOrders(self.user.login), self.user.login)
        for x in orders.lista:
            Label(self.main, text=f"{x[0]}").grid(row=b, column=0)
            Label(self.main, text=f"{x[1]}").grid(row=b, column=1)
            Label(self.main, text=f"{x[2]}").grid(row=b, column=2)
            b += 1
            print(x[0], x[1], x[2])
            # "%.2fzł" % round(prod.produkt.price, 2)

    def OrderData(self, klient):
        # klient.koszyk.loadFromDB()
        # klient.koszyk.obliczWartosc()
        # now = date.today()
        # now.strftime('%Y-%m-%d %H:%M:%S')
        # order = Zamowienie(klient.login, klient.koszyk.wartosc, klient.koszyk.zawartosc, now, 'waiting for authorization')
        self.ClearGUI()

        def createOrder(klient):
            imie = nameEntry.get()
            nazwisko = surnameEntry.get()
            email = emailEntry.get()
            miasto = cityEntry.get()
            ulica = streetEntry.get()
            lokal = houseEntry.get()
            kod = codeEntry.get()
            nrTel = telEntry.get()

            DB.UpdateClient(klient.login, imie, nazwisko, email,
                            nrTel, miasto, ulica, lokal, kod)

            klient.koszyk.loadFromDB()
            klient.koszyk.obliczWartosc()
            now = datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            daneKlienta = (imie, nazwisko, email,
                           nrTel, miasto, ulica, lokal, kod)
            order = Zamowienie(klient.login, ''.join(f"{str(e)};" for e in daneKlienta), klient.koszyk.wartosc,
                               ''.join(f"{str(e.produkt.id)}-{str(e.ilosc)};" for e in klient.koszyk.zawartosc), now, 'waiting for authorization')
            order.dodajZamowienie()
            DB.FromCartToOrder(klient.koszyk.zawartosc, klient.login)
            klient.koszyk.wartosc = 0
            # self.PanelKlienta()

        Label(self.main, text="imie").grid(row=2, column=0)
        nameEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        nameEntry.grid(row=2, column=1)
        nameEntry.insert(0, f"{klient.imie}")

        Label(self.main, text="nazwisko").grid(row=2, column=2)
        surnameEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        surnameEntry.grid(row=2, column=3)
        surnameEntry.insert(0, f"{klient.nazwisko}")

        Label(self.main, text="ulica").grid(row=3, column=0)
        streetEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        streetEntry.grid(row=3, column=1)
        streetEntry.insert(0, f"{klient.ulica}")

        Label(self.main, text="nr mieszkania").grid(row=3, column=2)
        houseEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        houseEntry.grid(row=3, column=3)
        houseEntry.insert(0, f"{klient.lokal}")

        Label(self.main, text="kod pocztowy").grid(row=4, column=0)
        codeEntry = Entry(self.main, fg="yellow", bg="blue", width=6)
        codeEntry.grid(row=4, column=1)
        codeEntry.insert(0, f"{klient.kodPocztowy}")

        Label(self.main, text="miasto").grid(row=4, column=2)
        cityEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        cityEntry.grid(row=4, column=3)
        cityEntry.insert(0, f"{klient.miasto}")

        Label(self.main, text="e-mail").grid(row=5, column=0)
        emailEntry = Entry(self.main, fg="yellow", bg="blue", width=20)
        emailEntry.grid(row=5, column=1)
        emailEntry.insert(0, f"{klient.email}")

        Label(self.main, text="nr telefonu").grid(row=5, column=2)
        telEntry = Entry(self.main, fg="yellow", bg="blue", width=12)
        telEntry.grid(row=5, column=3)
        telEntry.insert(0, f"{klient.nrTel}")

        Button(self.main,
               text="Zakończ",
               bg="blue",
               fg="yellow",
               command=lambda: createOrder(self.user),
               ).grid(row=7, column=1, pady=10)

        Button(self.main,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.CartList,
               ).grid(row=7, column=2)


# --------------- client --------------- #

    def PanelAdmina(self):  # ----- admin panel ----- #
        self.ClearGUI()
        menubar = Menu(self.window)
        menubar.add_cascade(label="Zarządzanie produktami",
                            command=lambda: self.EditProduct(Produkty.strona))
        menubar.add_separator()
        menubar.add_cascade(label="Zarządzanie rabatami",
                            command="")
        menubar.add_separator()
        menubar.add_cascade(label="Potwierdzanie zamówień",
                            command="")
        menubar.add_separator()
        menubar.add_cascade(label=f"{self.user.login}",
                            command="")
        menubar.add_separator()
        menubar.add_cascade(label="Wyloguj",
                            command=self.Wylogowywanie)
        self.window['menu'] = menubar

    def EditProduct(self, strona):
        self.ProductsList(strona)

        Label(self.main, text="Nazwa: ").grid(row=1, column=3, padx=5)
        nazwaInput = Entry(self.main, width=10)
        nazwaInput.grid(row=1, column=4, padx=5)

        Label(self.main, text="Cena: ").grid(row=1, column=5, padx=5)
        cenaInput = Entry(self.main, width=10)
        cenaInput.grid(row=1, column=6, padx=5)

        Label(self.main, text="Ilość: ").grid(row=1, column=7, padx=5)
        iloscInput = Entry(self.main, width=10)
        iloscInput.grid(row=1, column=8, padx=5)

        Label(self.main, text="Opis: ").grid(row=2, column=3, padx=5)

        frm = Frame(self.main, width=300, height=200, bg="blue")
        frm.place(x=400, y=55)
        text_area = scrolledtext.ScrolledText(frm,
                                              wrap=WORD,
                                              width=35,
                                              height=5,
                                              font=("Times New Roman", 15))

        text_area.grid(column=0)

        text_area.focus()

        def DodawnieProduktow():
            nazwa = nazwaInput.get()
            cena = cenaInput.get()
            cena = cena.replace(",", ".")
            cena = float(cena)
            ilosc = iloscInput.get()
            ilosc = int(ilosc)
            opis = text_area.get("1.0", 'end-1c')
            print(nazwa, cena, ilosc, opis)
            DB.AddProduct(nazwa, cena, ilosc, opis)
            Produkty.loadFromDB()

        Button(self.main,
               text="Dodaj",
               bg="blue",
               fg="yellow",
               command=DodawnieProduktow,
               width=10,
               ).grid(row=8, column=3)
