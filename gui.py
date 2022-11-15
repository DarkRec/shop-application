from tkinter import *
from guest import *
from index import search


class GUI:
    def __init__(self, window):
        self.window = window
        window.title("Internet Paper Shop Application")
        window.geometry('400x200')
        self.user = Gosc()
        self.GoscGUI()
        #self.label = Label(window, text="This is our first GUI!")
        # elf.label.pack()

        #self.greet_button = Button(window, text="Greet", command=self.greet)
        # self.greet_button.pack()

        #self.close_button = Button(window, text="Close", command=window.quit)
        # self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def GoscGUI(self):  # ----- guest ----- #
        Button(self.window,
               text="Logowanie",
               bg="blue",
               fg="yellow",
               width=15,
               height=2,
               font=("Arial", 15),
               command=self.PanelLogowania,  # lambda: PanelLogowania(user)
               ).pack()
        Button(self.window,
               text="Rejestracja",
               bg="blue",
               fg="yellow",
               width=25,
               height=5,
               command=self.PanelRejestracji,
               ).pack()

    def PanelLogowania(self):  # ----- login ----- #
        self.clear()

        def log_in():
            inputLogin = usernameEntry.get()
            inputPasswd = passwordEntry.get()
            print(inputLogin, inputPasswd)
            self.user = Gosc.logowanie(inputLogin, inputPasswd)
            if self.user.type == 'user':
                self.PanelKlienta()

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
               ).grid(row=7, column=0, pady=10)

    def PanelKlienta(self):  # ----- client panel ----- #
        self.clear()
        Label(self.window, text="Użytkownik:%s" %
              (self.user.login)).grid(row=0, column=0)
        Button(self.window,
               text="Lista Produktów",
               bg="blue",
               fg="yellow",
               command=self.ProductsList,
               width=15,
               ).grid(row=1, column=0, pady=10)

        Button(self.window,
               text="Konto",
               bg="blue",
               fg="yellow",
               command=self.Account,
               width=15,
               ).grid(row=1, column=1)

        Button(self.window,
               text="Koszyk",
               bg="blue",
               fg="yellow",
               command=self.CartList,
               width=15,
               ).grid(row=1, column=2)


# ----- products list ----- #

    def ProductsList(self):
        self.clear()
        self.PanelKlienta()
        strona = search.przegladanie()
        x = 3

        def Search():
            searchResults = search.wyszukaj(searchInput.get())
            self.clear()
            self.PanelKlienta()
            b = 2
            for x in searchResults:
                Label(self.window, text=f"{x.name}").grid(row=b, column=0)
                Label(self.window, text=f"{x.price}").grid(row=b, column=1)
                print(x.name, x.price)
                b += 1

        def AddToCart(prod):
            print(prod)

        Label(self.window, text="Wyszukaj: ").grid(row=2, column=0)
        searchInput = Entry(self.window, width=8)
        searchInput.grid(row=2, column=1)
        Button(self.window,
               text="Lista Produktów",
               bg="blue",
               fg="yellow",
               command=Search,
               width=15,
               ).grid(row=2, column=2, pady=10)

        for prod in strona:
            Label(self.window, text=f"{prod.name}").grid(row=x, column=0)
            # .grid(row=x, column=0)
            Label(self.window, text=f"{round(prod.price, 2)}").grid(
                row=x, column=1)
            Button(self.window, text="Dodaj do koszyka", command=lambda tempName=prod.name: AddToCart(
                tempName)).grid(row=x, column=2)
            # self.listaProduktow[x].wyswietl()
            x += 1

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
               command=self.Orders,
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
              text=f"Email: {self.user.daneKontaktowe(self.ser.login)[0]}"
              ).grid(row=6, column=0)

        Label(self.window,
              text=f"Nr Telefonu: {self.user.daneKontaktowe(self.user.login)[1]}"
              ).grid(row=6, column=1)

    def Orders(self):
        self.clear
        self.PanelKlienta()

        print("Zrobić zamówienia")
        Label(self.window,
              text=f"Brak zamówień"
              ).grid(row=3, column=0)

# ----- cart ----- #

    def CartList(self):
        self.clear
        self.PanelKlienta()

        myCart = cart.pokazZawartosc()
        cartUpdate = []
        x = 2
        for prod in myCart:
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
            x += 1

        endPrice = Label(self.window,
                         text=f"Suma: {cart.obliczWartosc()}")  # .grid(row=x, column=0)
        endPrice.grid(row=x, column=2)

        Button(self.window,
               text="Zapisz",
               bg="blue",
               fg="yellow",
               command=lambda: self.CartEdit(cartUpdate),
               width=7,
               ).grid(row=x+1, column=2, sticky=W)

        Button(self.window,
               text="Anuluj",
               bg="blue",
               fg="yellow",
               command=self.CartList,
               width=7,
               ).grid(row=x+1, column=2, sticky=E)

    # def CartEdit(update):
    #    global cart
    #    for x in update:
    #        for prod in Produkty:
    #            if prod.name == x[0]['text']:
    #                cart.zmien(prod, x[1].get())
    #                # print(x[0]['text'],x[1].get())
    #    self.CartList()

    # -------------------- orders --------------------#


root = Tk()
gui = GUI(root)
root.mainloop()
