#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk
import time

from DB.DB import DB
from app.Gosc import Gosc
from app.Klient import Klient
from app.Administrator import *
from app.Przegladanie import Produkty
from app.Zamowienie import *


class GUI:
    def PanelGoscia(self) -> None:  # ----- guest panel ----- # for guest
        self.ClearGUI()

        menubar = Menu(self.window)
        menubar.add_cascade(label="Lista Produktów",
                            command=lambda: self.ProductsList(1))
        menubar.add_separator()
        menubar.add_cascade(label="Logowanie",
                            command=self.PanelLogowania)
        menubar.add_separator()
        menubar.add_cascade(label="Rejestracja",
                            command=self.PanelRejestracji)  #

        self.window['menu'] = menubar

    def PanelLogowania(self) -> None:  # ----- login ----- # for guest
        self.ClearGUI()

        def log_in():
            inputLogin = usernameEntry.get()
            inputPasswd = passwordEntry.get()
            try:
                type = Gosc.logowanie(inputLogin, inputPasswd)

                if type == 'client':
                    self.user = Klient(inputLogin)
                    print('Logowanie użytkownika ', self.user.login)
                    self.PanelKlienta()
                elif type == "admin":
                    self.user = Administrator(inputLogin)
                    print('Logowanie administratora', self.user.login)
                    self.PanelAdmina()
                self.ProductsList(1)
            except:
                messagebox.showerror("Error", "Zły login lub hasło")

        Label(self.main, text="login", bg=self.mainColor).grid(row=0, column=0)
        usernameEntry = Entry(self.main, fg=self.fontColor,
                              bg=self.secondaryColor, width=20)
        usernameEntry.grid(row=0, column=1)

        Label(self.main, text="hasło", bg=self.mainColor).grid(row=1, column=0)
        passwordEntry = Entry(self.main, fg=self.fontColor,
                              bg=self.secondaryColor, width=20, show='*')
        passwordEntry.grid(row=1, column=1)

        Button(self.main,
               text="Logowanie",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=log_in,
               ).grid(row=3, column=0, pady=10)

        Button(self.main,
               text="Anuluj",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=self.PanelGoscia,
               ).grid(row=3, column=1)

    def PanelRejestracji(self) -> None:  # ----- rejestracja ----- # for guest
        self.ClearGUI()

        def rejestracja():

            try:
                self.user.rejestracja(usernameEntry.get(), passwordEntry.get(), nameEntry.get(), surnameEntry.get(),
                                      emailEntry.get(), cityEntry.get(), streetEntry.get(), houseEntry.get(),
                                      codeEntry.get(), telEntry.get())

                self.PanelLogowania()
            except:
                pass
                messagebox.showerror(
                    "Register Error", "Rejestracja niemożliwa, brak wymaganych danych")

        Label(self.main, text="login", bg=self.mainColor).grid(row=1, column=0)
        usernameEntry = Entry(self.main, fg=self.fontColor,
                              bg=self.secondaryColor, width=20)
        usernameEntry.grid(row=1, column=1)

        Label(self.main, text="hasło", bg=self.mainColor).grid(row=1, column=2)
        passwordEntry = Entry(self.main, fg=self.fontColor,
                              bg=self.secondaryColor, width=20, show='*')
        passwordEntry.grid(row=1, column=3)

        Label(self.main, text="imie", bg=self.mainColor).grid(row=2, column=0)
        nameEntry = Entry(self.main, fg=self.fontColor,
                          bg=self.secondaryColor, width=20)
        nameEntry.grid(row=2, column=1)

        Label(self.main, text="nazwisko",
              bg=self.mainColor).grid(row=2, column=2)
        surnameEntry = Entry(self.main, fg=self.fontColor,
                             bg=self.secondaryColor, width=20)
        surnameEntry.grid(row=2, column=3)

        Label(self.main, text="ulica", bg=self.mainColor).grid(row=3, column=0)
        streetEntry = Entry(self.main, fg=self.fontColor,
                            bg=self.secondaryColor, width=20)
        streetEntry.grid(row=3, column=1)

        Label(self.main, text="nr mieszkania",
              bg=self.mainColor).grid(row=3, column=2)
        houseEntry = Entry(self.main, fg=self.fontColor,
                           bg=self.secondaryColor, width=20)
        houseEntry.grid(row=3, column=3)

        Label(self.main, text="kod pocztowy",
              bg=self.mainColor).grid(row=4, column=0)

        def code_format(*args):
            if len(codeEntry.get()) > 2:
                code = codeEntry.get().replace("-", "")
                new_str = (f"{code[0:2]}-{code[2:]}")
            try:
                if len(new_str) > 6:
                    new_str = new_str[:6]
                e1_str.set(new_str)
            except:
                pass
            position = codeEntry.index(INSERT)
            codeEntry.icursor(position + 1)
        e1_str = tk.StringVar()
        codeEntry = Entry(self.main, fg=self.fontColor, bg=self.secondaryColor,
                          width=20, textvariable=e1_str)
        codeEntry.grid(row=4, column=1)
        codeEntry.bind("<KeyRelease>", code_format)

        Label(self.main, text="miasto", bg=self.mainColor).grid(row=4, column=2)
        cityEntry = Entry(self.main, fg=self.fontColor,
                          bg=self.secondaryColor, width=20)
        cityEntry.grid(row=4, column=3)

        Label(self.main, text="e-mail", bg=self.mainColor).grid(row=5, column=0)
        emailEntry = Entry(self.main, fg=self.fontColor,
                           bg=self.secondaryColor, width=20)
        emailEntry.grid(row=5, column=1)

        Label(self.main, text="nr telefonu",
              bg=self.mainColor).grid(row=5, column=2)

        def phone_format(*args):
            tel = telEntry.get().replace("-", "")
            if len(tel) > 9:
                new_str = (f"{tel[:3]}-{tel[3:6]}-{tel[6:10]}-{tel[10:]}")
            elif len(tel) > 6:
                new_str = (f"{tel[:3]}-{tel[3:6]}-{tel[6:]}")
            elif len(tel) > 3:
                new_str = (f"{tel[:3]}-{tel[3:]}")
            try:
                if len(new_str) > 11:
                    new_str = new_str[:11]
                number.set(new_str)
            except:
                pass
            position = telEntry.index(INSERT)
            telEntry.icursor(position + 1)
        number = tk.StringVar()
        telEntry = Entry(self.main, fg=self.fontColor, bg=self.secondaryColor,
                         width=20, textvariable=number)

        telEntry.grid(row=5, column=3)
        telEntry.bind("<KeyRelease>", phone_format)

        Button(self.main,
               text="Rejestracja",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=rejestracja,
               ).grid(row=7, column=1, pady=10)

        Button(self.main,
               text="Anuluj",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=self.PanelGoscia,
               ).grid(row=7, column=2)

    def PanelKlienta(self) -> None:  # ----- client panel ----- # for client
        menubar = Menu(self.window)
        menubar.add_cascade(label="Lista Produktów",
                            command=lambda: self.ProductsList(1))  #
        menubar.add_separator()
        menubar.add_cascade(label="Koszyk",
                            command=self.CartList)
        menubar.add_separator()

        usermenu = Menu(menubar, tearoff=0)
        usermenu.add_command(label="Dane", command=self.AccountData)
        usermenu.add_command(label="Zamówienia", command=self.Zamowienia)

        # command=self.Account,
        menubar.add_cascade(label=f"{self.user.login}", menu=usermenu)
        menubar.add_separator()
        menubar.add_cascade(label="Wyloguj",
                            command=self.Wylogowywanie)

        self.window['menu'] = menubar

    def PanelAdmina(self) -> None:  # ----- admin panel ----- # for admin
        self.ClearGUI()
        menubar = Menu(self.window)
        menubar.add_cascade(label="Zarządzanie produktami",
                            command=lambda: self.ProductsList(1))
        menubar.add_separator()
        menubar.add_cascade(label="Potwierdzanie zamówień",
                            command=self.OrdersList)
        menubar.add_separator()
        menubar.add_cascade(label=f"{self.user.login}",
                            command="")
        menubar.add_separator()
        menubar.add_cascade(label="Wyloguj",
                            command=self.Wylogowywanie)
        self.window['menu'] = menubar

    def ClearGUI(self) -> None:  # for everyone
        for widget in self.main.winfo_children():
            widget.destroy()

    # for everyone, specific options for admin and client
    def ProductsList(self, strona: int, mode: str | None = None, id: int | None = None) -> None:
        Produkty.strona = strona
        self.ClearGUI()

        x = 2

        def AddToCart(prodID, username, mode):
            DB.AddToCart(prodID, username)
            self.ProductsList(Produkty.strona, mode)

        def RemoveFromCart(prodID, username, mode):
            DB.RemoveFromCart(prodID, username)
            self.ProductsList(Produkty.strona, mode)

        def RemoveProduct(id, mode):
            DB.RemoveProduct(id)
            for x, i in enumerate(Produkty.lista):
                if i.id == id:
                    del Produkty.lista[x]
            self.ProductsList(Produkty.strona, mode)

        def EditProduct(id, mode):
            # DB.EditProduct(id)
            self.ProductsList(Produkty.strona, mode, id)

        Label(self.main, text="Wyszukaj: ", bg=self.mainColor, width=25, font=("Arial", 14)).grid(
            row=1, column=0, padx=25, pady=10)
        searchInput = Entry(self.main, width=14)
        searchInput.grid(row=1, column=1, padx=25, pady=10)

        Button(self.main,
               text="Search",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=lambda: self.ProductsList(
                   1, f"{searchInput.get()}!"),
               width=15, height=2, font=("Arial", 12)).grid(row=1, column=2, padx=25, pady=10)

        lista = []
        if mode is None:
            lista = Produkty.przegladanie()
        else:
            if mode[-1] == "!":
                lista = Produkty.wyszukaj(mode[:-1])
            else:
                lista = Produkty.filtruj(mode)

        for prod in lista:
            try:
                Label(self.main, text=f"{prod.nazwa}", height=1, bg=self.mainColor).grid(
                    row=x, column=0, pady=3)
                Label(self.main, text="%.2fzł" % round(prod.cena, 2), bg=self.mainColor).grid(
                    row=x, column=1, pady=3)
                if self.user.type == 'client':
                    Button(self.main, text="Info", fg=self.fontColor, bg=self.secondaryColor, command=lambda tempID=prod.id: self.ProductInfo(
                        tempID), width=8).grid(row=x, column=2, pady=3, sticky=W)
                else:
                    Button(self.main, text="Info", fg=self.fontColor, bg=self.secondaryColor, command=lambda tempID=prod.id: self.ProductInfo(
                        tempID), width=8).grid(row=x, column=2, pady=3)

            except:
                pass

            try:
                if self.user.type == 'client':
                    if (DB.ProductInCart(prod.id) == 0):
                        Button(self.main, text="Dodaj do koszyka",
                               bg="green", command=lambda tempID=prod.id: AddToCart(tempID, self.user.login, mode)).grid(row=x, column=2, sticky=E)
                    else:
                        Button(self.main, text="Usuń z koszyka", bg="red", command=lambda tempID=prod.id: RemoveFromCart(
                            tempID, self.user.login, mode)).grid(row=x, column=2, sticky=E)
                if self.user.type == 'admin':
                    Button(self.main, text="Usuń", bg="red",
                           command=lambda tempID=prod.id: RemoveProduct(tempID, mode)).grid(row=x, column=2, sticky=W)
                    Button(self.main, text="Edytuj", bg="blue",
                           command=lambda tempID=prod.id: EditProduct(tempID, mode)).grid(row=x, column=2, sticky=E)
            except:
                pass
            x += 1
        while x < Produkty.rozmiarStrony+2:
            Label(self.main, text=" ", height=1, bg=self.mainColor).grid(
                row=x, column=0, pady=3)
            x += 1

        def Prev(mode):
            Produkty.strona -= 1
            if Produkty.strona == 0:
                Produkty.strona = 1
            self.ProductsList(Produkty.strona, mode)

        def Next(mode):
            Produkty.strona += 1
            self.ProductsList(Produkty.strona, mode)

        Button(self.main,
               text="<",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=lambda: Prev(mode),
               width=5,
               ).grid(row=x, column=1, sticky=W, pady=10)

        Button(self.main,
               text=">",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=lambda: Next(mode),
               width=5,
               ).grid(row=x, column=1, sticky=E, pady=10)

        categories = DB.LoadCategories()
        cat = Frame(self.main, height=100, width=300,
                    borderwidth=2, bg=self.mainColor)
        cat.grid(row=x+1, column=0, pady=10)
        x = -1
        line = 3
        for i, j in enumerate(categories):
            if i % line == 0:
                x += 1
            Button(cat,
                   text=j[0],
                   bg=self.secondaryColor,
                   fg=self.fontColor,
                   command=lambda tempName=j[0]: self.ProductsList(
                       1, tempName),
                   width=12
                   ).grid(row=x, column=i-int(i/line)*line, sticky=E, pady=10, padx=5)

        if self.user.type == 'admin':
            self.EditProduct(1, id)

    def ProductInfo(self, id) -> None:  # for everyone
        self.ClearGUI()
        prod = Produkty.wystwietl(id)
        Label(self.main, text=f"{prod.nazwa}", font=(
            "Arial", 20), bg=self.mainColor).grid(row=0, column=0, padx=5, columnspan=2)

        Label(self.main, text=f"Cena: {prod.cena}zł", font=(
            "Arial", 12), bg=self.mainColor).grid(
            row=1, column=0, padx=5, columnspan=2)

        Label(self.main, text=f"Ilość: {prod.ilosc} szt.", font=(
            "Arial", 12), bg=self.mainColor).grid(
            row=2, column=0, padx=5, columnspan=2)

        Label(self.main, text=f"{prod.opis}", width=50, bg=self.mainColor, wraplength=300, justify="center").grid(
            row=3, column=0, padx=5, columnspan=2)

        Button(self.main,
               text="Cofnij",
               bg=self.secondaryColor,
               fg=self.fontColor,
               width=15,
               command=lambda: self.ProductsList(Produkty.strona)
               ).grid(row=4, column=0)

        canvas_for_image = Canvas(
            self.main, height=200, width=200, highlightbackground="black", highlightthickness=2)  # , bg='green'
        canvas_for_image.grid(
            row=0, column=3, sticky='nesw', padx=0, pady=0, rowspan=3)

        try:
            image = Image.open(f'./img/{prod.nazwa}.jpg')
        except:
            try:
                image = Image.open(f'./img/{prod.nazwa}.png')
            except:
                image = Image.open(f'./img/blank.png')
        canvas_for_image.image = ImageTk.PhotoImage(
            image.resize((200, 200), Image.ANTIALIAS))
        canvas_for_image.create_image(
            0, 0, image=canvas_for_image.image, anchor='nw')

    def Search(self, searchResults: str) -> None:  # for everyone
        self.ClearGUI()

        Button(self.main,
               text="Cofnij",
               bg=self.secondaryColor,
               fg=self.mainColor,
               width=15,
               command=lambda: self.ProductsList(Produkty.strona),
               ).grid(row=1, column=2)
        Label(self.main, text=" ", bg=self.mainColor,
              height=1).grid(row=1, column=0)

        b = 2
        for x in searchResults:
            Label(self.main, text=f"{x.nazwa}", bg=self.mainColor,
                  height=1, width=10).grid(row=b, column=0, padx=25)
            Label(self.main, text="%.2fzł" %
                  round(x.cena, 2), bg=self.mainColor).grid(row=b, column=1, padx=25)
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
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=Prev,
               width=5,
               ).grid(row=x, column=1, sticky=W, pady=10)

        Button(self.main,
               text=">",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=Next,
               width=5,
               ).grid(row=x, column=1, sticky=E, pady=10)

    def Zamowienia(self) -> None:  # for client
        self.ClearGUI()

        Label(self.main, text="cena", bg=self.mainColor,
              font=("Arial", 12)).grid(row=2, column=0, padx=5)
        Label(self.main, text="data zamówienia",
              bg=self.mainColor, font=("Arial", 12)).grid(row=2, column=1, padx=5)
        Label(self.main, text="status", bg=self.mainColor,
              font=("Arial", 12)).grid(row=2, column=2, padx=5)
        b = 3
        orders = DB.loadUserOrders(self.user.login)
        for x in orders:
            Label(self.main, text=f"{x[1]} zł",
                  bg=self.mainColor).grid(row=b, column=0)
            Label(self.main, text=f"{x[2]}",
                  bg=self.mainColor).grid(row=b, column=1)
            Label(self.main, text=f"{x[3]}",
                  bg=self.mainColor).grid(row=b, column=2)

            def cancel(id: int):
                DB.CancelOrder(id)
                self.Zamowienia()

            Button(self.main,
                   text="Info",
                   bg=self.secondaryColor,
                   fg=self.fontColor,
                   command=lambda tempID=x[0]: self.OrderInfo(tempID),
                   ).grid(row=b, column=3, pady=10)

            if x[3] == "waiting for payment":
                Button(self.main,
                       text="Zapłać za pobraniem",
                       bg=self.secondaryColor,
                       fg=self.fontColor,
                       command=lambda tempID=x[0]: self.Payment(tempID, False),
                       ).grid(row=b, column=4, pady=10)
                Button(self.main,
                       text="Zapłać przelewem",
                       bg=self.secondaryColor,
                       fg=self.fontColor,
                       command=lambda tempID=x[0]: self.Payment(tempID),
                       ).grid(row=b, column=5, pady=10)
            elif x[3] == "waiting for authorization" or x[3] == "in progress":
                Button(self.main,
                       text="Anuluj zamówienie",
                       bg=self.secondaryColor,
                       fg=self.fontColor,
                       command=lambda tempID=x[0]: cancel(tempID),
                       ).grid(row=b, column=4, pady=10)
            b += 1

    def OrderData(self, klient: Klient) -> None:  # for client
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
            daneKlienta = (imie, nazwisko, email,
                           nrTel, miasto, ulica, lokal, kod)
            order = Zamowienie(klient.login, ''.join(f"{str(e)};" for e in daneKlienta), klient.koszyk.wartosc,
                               ''.join(
                                   f"{str(e.produkt.id)}-{str(e.ilosc)};" for e in klient.koszyk.zawartosc),
                               time.strftime('%Y-%m-%d %H:%M:%S'), 'waiting for payment')
            order.dodajZamowienie()
            DB.FromCartToOrder(klient.koszyk.zawartosc, klient.login)
            klient.koszyk.wartosc = 0
            self.ProductsList(1)

        Label(self.main, text="imie", bg=self.mainColor).grid(row=2, column=0)
        nameEntry = Entry(self.main, bg=self.secondaryColor,
                          fg=self.fontColor, width=20)
        nameEntry.grid(row=2, column=1)
        nameEntry.insert(0, f"{klient.imie}")

        Label(self.main, text="nazwisko",
              bg=self.mainColor).grid(row=2, column=2)
        surnameEntry = Entry(self.main, bg=self.secondaryColor,
                             fg=self.fontColor, width=20)
        surnameEntry.grid(row=2, column=3)
        surnameEntry.insert(0, f"{klient.nazwisko}")

        Label(self.main, text="ulica", bg=self.mainColor).grid(row=3, column=0)
        streetEntry = Entry(self.main, bg=self.secondaryColor,
                            fg=self.fontColor, width=20)
        streetEntry.grid(row=3, column=1)
        streetEntry.insert(0, f"{klient.ulica}")

        Label(self.main, text="nr mieszkania",
              bg=self.mainColor).grid(row=3, column=2)
        houseEntry = Entry(self.main, bg=self.secondaryColor,
                           fg=self.fontColor, width=20)
        houseEntry.grid(row=3, column=3)
        houseEntry.insert(0, f"{klient.nr_mieszkania}")

        Label(self.main, text="kod pocztowy",
              bg=self.mainColor).grid(row=4, column=0)
        codeEntry = Entry(self.main, bg=self.secondaryColor,
                          fg=self.fontColor, width=6)
        codeEntry.grid(row=4, column=1)
        codeEntry.insert(0, f"{klient.kod_Pocztowy}")

        Label(self.main, text="miasto", bg=self.mainColor).grid(row=4, column=2)
        cityEntry = Entry(self.main, bg=self.secondaryColor,
                          fg=self.fontColor, width=20)
        cityEntry.grid(row=4, column=3)
        cityEntry.insert(0, f"{klient.miasto}")

        Label(self.main, text="e-mail", bg=self.mainColor).grid(row=5, column=0)
        emailEntry = Entry(self.main, bg=self.secondaryColor,
                           fg=self.fontColor, width=20)
        emailEntry.grid(row=5, column=1)
        emailEntry.insert(0, f"{klient.email}")

        Label(self.main, text="nr telefonu",
              bg=self.mainColor).grid(row=5, column=2)
        telEntry = Entry(self.main, bg=self.secondaryColor,
                         fg=self.fontColor, width=12)
        telEntry.grid(row=5, column=3)
        telEntry.insert(0, f"{klient.nr_Telefonu}")

        Button(self.main,
               text="Zakończ",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=lambda: createOrder(self.user),
               ).grid(row=7, column=1, pady=10)

        Button(self.main,
               text="Anuluj",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=self.CartList,
               ).grid(row=7, column=2)

    def AccountData(self) -> None:  # for client
        self.ClearGUI()

        Label(self.main,
              text=f"Imie: {self.user.imie}", bg=self.mainColor
              ).grid(row=3, column=0)  # .grid(row=x, column=0)

        Label(self.main,
              text=f"Nazwisko: {self.user.nazwisko}", bg=self.mainColor
              ).grid(row=3, column=1)

        Label(self.main,
              text=f"Ulica: {self.user.ulica}", bg=self.mainColor
              ).grid(row=4, column=0)

        Label(self.main,
              text=f"Nr mieszkania: {self.user.nr_mieszkania}", bg=self.mainColor
              ).grid(row=4, column=1)

        Label(self.main,
              text=f"Kod Pocztowy: {self.user.kod_Pocztowy}", bg=self.mainColor
              ).grid(row=5, column=0)

        Label(self.main,
              text=f"Miasto: {self.user.miasto}", bg=self.mainColor
              ).grid(row=5, column=1)

        Label(self.main,
              text=f"Email: {self.user.email}", bg=self.mainColor
              ).grid(row=6, column=0)

        Label(self.main,
              text=f"Nr Telefonu: {self.user.nr_Telefonu}", bg=self.mainColor
              ).grid(row=6, column=1)

    def CartList(self) -> None:  # for client
        self.ClearGUI()
        cartUpdate = []
        x = 2
        self.user.koszyk.loadFromDB()
        for prod in self.user.koszyk.zawartosc:
            cartName = Label(
                self.main, text=f"{prod.produkt.nazwa}", bg=self.mainColor)
            cartName.grid(row=x, column=0, pady=3)

            cartPrice = Label(self.main, text="%.2fzł" % round(
                prod.produkt.cena, 2), bg=self.mainColor)
            cartPrice.grid(row=x, column=1)

            cartNumber = Entry(self.main, width=8)
            cartNumber.insert(0, f"{prod.ilosc}")
            cartNumber.grid(row=x, column=2)
            cartUpdate.append((cartName, cartNumber))

            def Remove(prodID, username):
                DB.RemoveFromCart(prodID, username)
                self.CartList()

            Button(self.main, text="X", bg="#FF0000", fg=self.mainColor, width=3, command=lambda tempID=prod.produkt.id: Remove(
                tempID, self.user.login)).grid(row=x, column=3)
            Button(self.main, text="Info", fg=self.fontColor, bg=self.secondaryColor, command=lambda tempID=prod.produkt.id: self.ProductInfo(
                tempID), width=8).grid(row=x, column=4, padx=5)

            x += 1

        # .grid(row=x, column=0)
        endPrice = Label(
            self.main, text=f"Suma:  {self.user.koszyk.obliczWartosc()}", bg=self.mainColor)
        endPrice.grid(row=x, column=1, pady=3)

        Button(self.main,
               text="Zapisz",
               bg=self.secondaryColor,
               fg=self.mainColor,
               command=lambda: self.CartEdit(cartUpdate),
               width=6,
               ).grid(row=x+1, column=2, sticky=W)

        Button(self.main,
               text="Anuluj",
               bg=self.secondaryColor,
               fg=self.mainColor,
               command=self.CartList,
               width=6,
               ).grid(row=x+1, column=2, sticky=E)

        Button(self.main,
               text="Złóż zamówiene",
               bg=self.secondaryColor,
               fg=self.mainColor,
               command=lambda: self.OrderData(self.user),
               width=15,
               ).grid(row=x+2, column=2, pady=5)

    def CartEdit(self, update: str) -> None:  # for client
        for x in update:
            self.user.koszyk.zmien(x[0]['text'], x[1].get())
        self.CartList()

    def Payment(self, id: int, transfer: bool | None = True) -> None:  # for client
        self.ClearGUI()

        def pay():
            name = nameEntry.get()
            surname = surnameEntry.get()
            bank = street = house = code = city = typ = None
            if transfer:
                bank = bankEntry.get()
                typ = 'przelew'
            else:
                street = streetEntry.get()
                house = houseEntry.get()
                code = codeEntry.get()
                city = cityEntry.get()
                typ = 'dostawa'
            DB.Paid(id, typ)
            self.Zamowienia()

        Label(self.main, text="imie", bg=self.mainColor).grid(row=0, column=0)
        nameEntry = Entry(self.main, fg=self.fontColor,
                          bg=self.secondaryColor, width=20)
        nameEntry.grid(row=0, column=1)

        Label(self.main, text="nazwisko",
              bg=self.mainColor).grid(row=0, column=2)
        surnameEntry = Entry(self.main, fg=self.fontColor,
                             bg=self.secondaryColor, width=20)
        surnameEntry.grid(row=0, column=3)

        if transfer:
            Label(self.main, text="nr konta",
                  bg=self.mainColor).grid(row=1, column=0)
            bankEntry = Entry(self.main, fg=self.fontColor,
                              bg=self.secondaryColor, width=40)
            bankEntry.grid(row=1, column=1, columnspan=3)
        else:
            Label(self.main, text="ulica", bg=self.mainColor).grid(
                row=1, column=0)
            streetEntry = Entry(self.main, fg=self.fontColor,
                                bg=self.secondaryColor, width=20)
            streetEntry.grid(row=1, column=1)

            Label(self.main, text="nr mieszkania",
                  bg=self.mainColor).grid(row=1, column=2)
            houseEntry = Entry(self.main, fg=self.fontColor,
                               bg=self.secondaryColor, width=20)
            houseEntry.grid(row=1, column=3)

            Label(self.main, text="kod pocztowy",
                  bg=self.mainColor).grid(row=2, column=0)
            codeEntry = Entry(self.main, fg=self.fontColor,
                              bg=self.secondaryColor, width=20)
            codeEntry.grid(row=2, column=1)

            Label(self.main, text="miasto",
                  bg=self.mainColor).grid(row=2, column=2)
            cityEntry = Entry(self.main, fg=self.fontColor,
                              bg=self.secondaryColor, width=20)
            cityEntry.grid(row=2, column=3)

        Button(self.main,
               text="Zatwierdź",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=pay,
               ).grid(row=3, column=1, pady=10)

        Button(self.main,
               text="Cofnij",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=self.Zamowienia,
               ).grid(row=3, column=2, pady=10)

    def OrderInfo(self, id) -> None:  # for admin and client
        self.ClearGUI()
        info = DB.OrderInfo(id)

        Label(self.main,
              text=f"Imie: {info[0].split(';')[0]}", bg=self.mainColor
              ).grid(row=3, column=0)  # .grid(row=x, column=0)

        Label(self.main,
              text=f"Nazwisko: {info[0].split(';')[1]}", bg=self.mainColor
              ).grid(row=3, column=1)

        Label(self.main,
              text=f"Ulica: {info[0].split(';')[6]}", bg=self.mainColor
              ).grid(row=4, column=0)

        Label(self.main,
              text=f"Nr mieszkania: {info[0].split(';')[7]}", bg=self.mainColor
              ).grid(row=4, column=1)

        Label(self.main,
              text=f"Kod Pocztowy: {info[0].split(';')[8]}", bg=self.mainColor
              ).grid(row=5, column=0)

        Label(self.main,
              text=f"Miasto: {info[0].split(';')[5]}", bg=self.mainColor
              ).grid(row=5, column=1)

        Label(self.main,
              text=f"Email: {info[0].split(';')[3]}", bg=self.mainColor
              ).grid(row=6, column=0)

        Label(self.main,
              text=f"Nr Telefonu: {info[0].split(';')[4]}", bg=self.mainColor
              ).grid(row=6, column=1)

        Label(self.main,
              text=f"Status: {info[3]}", bg=self.mainColor
              ).grid(row=7, column=0)
        Label(self.main,
              text=f"Utworzone: {info[4]}", bg=self.mainColor
              ).grid(row=7, column=1)
        Label(self.main,
              text=f"==================================", bg=self.mainColor
              ).grid(row=8, column=0, columnspan=2)

        x = 9
        for i in info[2].split(';'):
            try:
                temp = DB.SelectProduct(i.split('-')[0])
                Label(self.main,
                      text=f"{temp[0]}", bg=self.mainColor
                      ).grid(row=x, column=0)
                Label(self.main,
                      text=f"{i.split('-')[1]}", bg=self.mainColor
                      ).grid(row=x, column=1)
            except:
                pass
            x += 1

    def Wylogowywanie(self) -> None:  # for admin and client
        self.user = Gosc()
        self.PanelGoscia()

    def OrdersList(self) -> None:  # for admin
        self.ClearGUI()

        Label(self.main, text="użytkownik", bg=self.mainColor,
              font=("Arial", 12)).grid(row=2, column=0, padx=5)
        Label(self.main, text="cena", bg=self.mainColor,
              font=("Arial", 12)).grid(row=2, column=1, padx=5)
        Label(self.main, text="data zamówienia",
              bg=self.mainColor, font=("Arial", 12)).grid(row=2, column=2, padx=5)
        Label(self.main, text="status", bg=self.mainColor,
              font=("Arial", 12)).grid(row=2, column=3, padx=5)
        b = 3
        orders = DB.loadOrders()
        for x in orders:
            Label(self.main, text=f"{self.user.login} zł",
                  bg=self.mainColor).grid(row=b, column=0)
            Label(self.main, text=f"{x[1]} zł",
                  bg=self.mainColor).grid(row=b, column=0)
            Label(self.main, text=f"{x[2]}",
                  bg=self.mainColor).grid(row=b, column=1)
            Label(self.main, text=f"{x[3]}",
                  bg=self.mainColor).grid(row=b, column=2)

            def auth(id: int):
                DB.Authorization(id)
                self.OrdersList()

            Button(self.main,
                   text="Info",
                   bg=self.secondaryColor,
                   fg=self.fontColor,
                   command=lambda tempID=x[0]: self.OrderInfo(tempID),
                   ).grid(row=b, column=3, pady=10)
            if x[3] == "waiting for authorization":
                Button(self.main,
                       text="Zatwierdź",
                       bg=self.secondaryColor,
                       fg=self.fontColor,
                       command=lambda tempID=x[0]: auth(tempID),
                       ).grid(row=b, column=4, pady=10)
            b += 1

    def EditProduct(self, strona, id: int | None = None) -> None:  # for admin

        def EdytowanieProduktow(id):
            nazwa = nazwaInput.get()
            cena = cenaInput.get()
            cena = cena.replace(",", ".")
            try:
                cena = float(cena)
                ilosc = iloscInput.get()
                ilosc = int(ilosc)
                kategoria = kategoriaInput.get()
                opis = text_area.get("1.0", 'end-1c')
                DB.EditProduct(id, nazwa, cena, ilosc, opis, kategoria)
                Produkty.loadFromDB()
                self.ProductsList(1)
            except:
                print("błąd")

        nazwa = kategoria = opis = ""
        ilosc = cena = 0
        if id is not None:
            prod = DB.SelectProduct(id)
            nazwa = prod[0]
            cena = prod[1]
            ilosc = prod[2]
            kategoria = prod[3]
            opis = prod[4]
            Button(self.main,
                   text="Edytuj",
                   bg=self.secondaryColor,
                   fg=self.fontColor,
                   command=lambda: EdytowanieProduktow(id),
                   width=10,
                   ).place(x=790, y=260)

        Label(self.main, text="Nazwa: ", bg=self.mainColor, width=10).grid(
            row=1, column=3, padx=10)
        nazwaInput = Entry(self.main, width=44)
        nazwaInput.insert(END, nazwa)
        nazwaInput.grid(row=1, column=4, padx=5, columnspan=3)

        Label(self.main, text="Cena: ", bg=self.mainColor).grid(
            row=2, column=3, padx=5)
        cenaInput = Entry(self.main, width=15)
        cenaInput.insert(END, cena)
        cenaInput.grid(row=2, column=4, padx=5)

        Label(self.main, text="Ilość: ", bg=self.mainColor, width=10).grid(
            row=2, column=5, padx=5)
        iloscInput = Entry(self.main, width=15)
        iloscInput.insert(END, ilosc)
        iloscInput.grid(row=2, column=6, padx=5)

        Label(self.main, text="Kategoria: ", bg=self.mainColor, width=10).grid(
            row=3, column=5, padx=5)
        kategoriaInput = Entry(self.main, width=15)
        kategoriaInput.insert(END, kategoria)
        kategoriaInput.grid(row=3, column=6, padx=5)

        Label(self.main, text="Opis: ", bg=self.mainColor).grid(
            row=4, column=3, padx=5)

        frm = Frame(self.main, bg=self.secondaryColor)
        frm.place(x=755, y=135)
        text_area = scrolledtext.ScrolledText(frm,
                                              wrap=WORD,
                                              width=28,
                                              height=5,
                                              font=("Times New Roman", 15))
        text_area.insert(END, opis)
        text_area.grid(column=0)

        text_area.focus()

        def DodawnieProduktow():
            nazwa = nazwaInput.get()
            cena = cenaInput.get()
            cena = cena.replace(",", ".")
            try:
                cena = float(cena)
                ilosc = iloscInput.get()
                ilosc = int(ilosc)
                kategoria = kategoriaInput.get()
                opis = text_area.get("1.0", 'end-1c')
                DB.AddProduct(nazwa, cena, ilosc, opis, kategoria)
                Produkty.loadFromDB()
                self.ProductsList(1)
            except:
                print("błąd")

        Button(self.main,
               text="Dodaj",
               bg=self.secondaryColor,
               fg=self.fontColor,
               command=DodawnieProduktow,
               width=10,
               ).place(x=690, y=260)
        # .grid(row=8, column=3)
        return

    def ConfigGUI(self, window):  # for almost every method
        self.user = Gosc()

        self.mainColor = "#F5F2D2"
        self.secondaryColor = "#36352E"
        self.fontColor = "#DBD9BD"

        self.window = window
        window.title("Internet Paper Shop Application")
        window.geometry('1280x720')
        window.option_add('*tearOff', FALSE)
        window['bg'] = self.mainColor

        self.main = Frame(window, height=500)
        self.main.place(x=5, y=0)
        self.main['bg'] = self.mainColor

    def __init__(self, window):
        self.ConfigGUI(window)
        self.PanelGoscia()
