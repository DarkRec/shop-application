from tkinter import *
import mysql.connector
from asyncio.windows_events import NULL
#import tkinter as tk
#window = tk.Tk()
from datetime import date


class Gosc:
    def rejestracja(login, haslo, imie, nazwisko, email, miasto, ulica, lokal, kod, nrTel):
        cursor = connection.cursor()
        # cursor.execute("IF NOT EXISTS (SELECT 1 FROM users WHERE username = '%s')BEGIN INSERT INTO users ('imie', 'nazwisko', 'email', 'miasto', 'ulica', 'lokal', 'kodPocztowy', nrTelefonu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) END" % (login , imie, nazwisko, email, miasto, ulica, lokal, kod, nrTel))
        try:
            cursor.execute(
                "SELECT type FROM users WHERE username = '%s'" % (login))
            if cursor.fetchone()[0] == 'user':
                print('Taki użytkownik już istnieje')
        except:
            print('Rejestracja użytkownika', login)
        cursor.execute("INSERT INTO klienci (`username`, `imie`, `nazwisko`, `email`, `miasto`, `ulica`, `lokal`, `kodPocztowy`, nrTelefonu) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
            login, imie, nazwisko, email, miasto, ulica, lokal, kod, nrTel))
        cursor.execute(
            "INSERT INTO users (`username`, `password`) VALUES ('%s', '%s');" % (login, haslo))
        connection.commit()

    def logowanie(login, haslo):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT type FROM users WHERE username = '%s' AND password LIKE '%s'" % (login, haslo))
        fetchedRow = cursor.fetchone()
        try:
            if fetchedRow[0] == 'user':
                global user
                user = Klient(login)
                global cart
                cart = Koszyk(login)
                cart.loadFromDB()
                PanelKlienta()
                print('Logowanie użytkownika ', login)
                return 'user'
            elif fetchedRow[0] == 'admin':
                print('Logowanie administratora', login)
                return 'admin'
        except:
            print("Błąd logowania")
            return 'guest'


class Klient:
    def __init__(self, login) -> None:
        self.login = login
        self.koszyk = Koszyk(login)
        self.imie = self.daneOsobowe(login)[0]
        self.nazwisko = self.daneOsobowe(login)[1]
        self.email = self.daneKontaktowe(login)[0]
        self.miasto = self.daneKontaktowe(login)[1]
        self.ulica = self.daneKontaktowe(login)[2]
        self.lokal = self.daneKontaktowe(login)[3]
        self.kodPocztowy = self.daneKontaktowe(login)[4]
        self.nrTel = self.daneKontaktowe(login)[5]
        self.wypiszDane()

    def daneOsobowe(self, login):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT imie, nazwisko FROM klienci WHERE username = '%s'" % (login))
        fetchedRow = cursor.fetchone()
        return fetchedRow

    def daneKontaktowe(self, login):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT email, nrTelefonu, miasto, ulica, lokal, kodPocztowy FROM klienci WHERE username = '%s'" % (login))
        fetchedRow = cursor.fetchone()
        return fetchedRow

    def edytujDane(self):
        rodzaj = input("Co chcesz edytowac?  ")
        wartosc = input("Nowa wartosc  ")
        cursor = connection.cursor()
        match rodzaj:
            case "email":
                self.email = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "email", wartosc, self.login))
            case "ulica":
                self.ulica = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "ulica", wartosc, self.login))
            case "lokal":
                self.lokal = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "lokal", wartosc, self.login))
            case "Kod pocztowy":
                self.kodPocztowy = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "kodPocztowy", wartosc, self.login))
            case "Nr telefonu":
                self.nrTel = wartosc
                cursor.execute("UPDATE klienci SET '%s' = '%s' WHERE (`username` = '%s');" % (
                    "nrTelefonu", wartosc, self.login))

    def wypiszDane(self):
        print(self.imie, self.nazwisko)
        print(self.miasto, self.ulica, self.lokal, self.kodPocztowy)
        print(self.email, self.nrTel)


class ElementKoszyka:
    def __init__(self, produkt, ilosc):
        self.produkt = produkt
        self.ilosc = ilosc


class Koszyk:
    def __init__(self, login):
        self.zawartosc = []
        self.wartosc = 0
        self.login = login

    def loadFromDB(self):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT produkt, koszyk.ilosc, cena, opis FROM koszyk INNER JOIN produkty ON koszyk.produkt = produkty.nazwa WHERE username = '%s';" % (self.login))
        fetchedRows = cursor.fetchall()

        self.zawartosc = []
        for row in fetchedRows:
            self.zawartosc.append(ElementKoszyka(
                Produkt(row[0], row[2], row[3]), row[1]))

    def obliczWartosc(self):
        self.wartosc = 0
        for el in self.zawartosc:
            self.wartosc += (el.produkt.price * el.ilosc)
        return  "%.2fzł" % round(self.wartosc, 2)
        # print(self.wartosc)

    def pokazZawartosc(self):
        for el in self.zawartosc:
            # el.produkt.info()
            print(el.produkt.name, "%.2fzł" %
                  round(el.produkt.price, 2), "-", el.ilosc, "szt")
        return self.zawartosc

    def dodaj(self, produkt, ilosc):
        self.loadFromDB()
        for el in self.zawartosc:
            if produkt.name == el.produkt.name:
                if ilosc > 0:
                    self.zwieksz(el, ilosc)
                return 0
        if ilosc > 0:
            self.zawartosc.append(ElementKoszyka(produkt, ilosc))
        self.obliczWartosc()
        #cursor = connection.cursor()
        # cursor.execute(
        #    "INSERT INTO users (`username`, `password`) VALUES ('%s', '%s');" % (login, haslo))
        # connection.commit()

    def usun(self, produkt):
        for el in self.zawartosc:
            if produkt.name == el.produkt.name:
                self.zawartosc.remove(el)
        self.obliczWartosc()

    def zwieksz(self, prod, ilosc):
        if (ilosc > 0):
            prod.ilosc += ilosc
            connection.cursor().execute("UPDATE `koszyk` SET `ilosc` = '%i' WHERE (`username` = '%s' AND `produkt` = '%s');" %
                                        (prod.ilosc, self.login, prod.produkt.name))
            connection.commit()
            self.obliczWartosc()

    def zmniejsz(self, prod, ilosc):
        if (ilosc > 0):
            for el in self.zawartosc:
                if prod.name == el.produkt.name:
                    el.ilosc -= ilosc
                    if el.ilosc < 1:
                        el.ilosc = 1
                    connection.cursor().execute("UPDATE `koszyk` SET `ilosc` = '%i' WHERE (`username` = '%s' AND `produkt` = '%s');" %
                                                (el.ilosc, self.login, el.produkt.name))
                    connection.commit()
                    self.obliczWartosc()

    def zmien(self, prod, ilosc):
        for el in self.zawartosc:
            if prod.name == el.produkt.name:
                el.ilosc = int(ilosc)
                if el.ilosc < 1:
                    el.ilosc = 1

                cursor = connection.cursor()
                cursor.execute(
                    f"SELECT ilosc FROM produkty WHERE nazwa = '{prod.name}';")
                fetchedRow = cursor.fetchone()
                if el.ilosc > int(fetchedRow[0]):
                    el.ilosc = int(fetchedRow[0])
                connection.cursor().execute("UPDATE `koszyk` SET `ilosc` = '%i' WHERE (`username` = '%s' AND `produkt` = '%s');" %
                                            (el.ilosc, self.login, el.produkt.name))
                connection.commit()
                self.obliczWartosc()

    def czyszczenie(self):
        self.zawartosc = []
        self.wartosc = 0


class Produkt:
    def __init__(self, name, price: float, opis):
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


class Zamowienie:
    def __init__(self,ProductList, value, status, date):
        self.ListaProduktow = ProductList
        self.wartosc = value
        self.status = status
        self.data = date

    def wypisz(self):
        print("======")
        print(f"wartosc - {self.wartosc} , status - {self.status}" )
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
            


connection = mysql.connector.connect(
    database='sklep',
    host="localhost",
    user="root",
    password="admin"
)


#cursor = connection.cursor()
#cursor.execute("SELECT lista, wartosc, stan, utworzenie FROM zamowienia;")
#orders = cursor.fetchall()
#order = orders[0]
#print(order)
#a = Zamowienie(order[0], order[1], order[2], order[3])
#a.wypisz()



def loadProductsFromDB(Produkty):
    cursor = connection.cursor()
    #result = cursor.execute(mySql_Create_Table_Query)
    cursor.execute("SELECT nazwa, cena FROM Produkty")
    fetchedRows = cursor.fetchall()

    for row in fetchedRows:
        nazwa = row[0]
        cena = row[1]
        try:
            opis = row[2]

        except:
            opis = ""
        Produkty.append(Produkt(nazwa, cena, opis))
    # if connection.is_connected():
    #    cursor.close()
    #    connection.close()
        #print("MySQL connection is closed")
    return Produkty


# ------------------- Basic variables ------------------#

Produkty = []
loadProductsFromDB(Produkty)
search = Przegladanie(Produkty)
user = Gosc

# ----------------------------------- GUI -----------------------------------#

window = Tk()
window.geometry('400x200')
window.title('Tkinter Login Form')


def clear():
    for widget in window.winfo_children():
        widget.destroy()

# -------------------- guest --------------------#


def GoscGUI():
    Button(window,
           text="Logowanie",
           bg="blue",
           fg="yellow",
           width=15,
           height=2,
           font=("Arial", 15),
           command=PanelLogowania,        #lambda: PanelLogowania(user)
           ).pack()
    Button(window,
           text="Rejestracja",
           bg="blue",
           fg="yellow",
           width=25,
           height=5,
           command=PanelRejestracji,
           ).pack()

    window.mainloop()

# -------------------- login --------------------#


def PanelLogowania():
    clear()

    def log_in():
        inputLogin = usernameEntry.get()
        inputPasswd = passwordEntry.get()
        print(inputLogin, inputPasswd)
        Gosc.logowanie(inputLogin, inputPasswd)

    Label(window, text="login").grid(row=0, column=0)
    usernameEntry = Entry(window, fg="yellow", bg="blue", width=20)
    usernameEntry.grid(row=0, column=1)

    Label(window, text="hasło").grid(row=1, column=0)
    passwordEntry = Entry(window, fg="yellow", bg="blue", width=20, show='*')
    passwordEntry.grid(row=1, column=1)

    Button(window,
           text="Logowanie",
           bg="blue",
           fg="yellow",
           command=log_in,
           ).grid(row=3, column=0, pady=10)

    # side = LEFT / RIGHT
    # .pack(pady)

    window.mainloop()

# -------------------- register --------------------#


def PanelRejestracji():
    clear()

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
            return Gosc.logowanie(login, haslo)

    Label(window, text="login").grid(row=1, column=0)
    usernameEntry = Entry(window, fg="yellow", bg="blue", width=20)
    usernameEntry.grid(row=1, column=1)

    Label(window, text="hasło").grid(row=1, column=2)
    passwordEntry = Entry(window, fg="yellow", bg="blue", width=20, show='*')
    passwordEntry.grid(row=1, column=3, pady=10)

    Label(window, text="imie").grid(row=2, column=0)
    nameEntry = Entry(window, fg="yellow", bg="blue", width=20)
    nameEntry.grid(row=2, column=1)

    Label(window, text="nazwisko").grid(row=2, column=2)
    surnameEntry = Entry(window, fg="yellow", bg="blue", width=20)
    surnameEntry.grid(row=2, column=3)

    Label(window, text="ulica").grid(row=3, column=0)
    streetEntry = Entry(window, fg="yellow", bg="blue", width=20)
    streetEntry.grid(row=3, column=1)

    Label(window, text="nr mieszkania").grid(row=3, column=2)
    houseEntry = Entry(window, fg="yellow", bg="blue", width=20)
    houseEntry.grid(row=3, column=3)

    Label(window, text="kod pocztowy").grid(row=4, column=0)
    codeEntry = Entry(window, fg="yellow", bg="blue", width=6)
    codeEntry.grid(row=4, column=1)

    Label(window, text="miasto").grid(row=4, column=2)
    cityEntry = Entry(window, fg="yellow", bg="blue", width=20)
    cityEntry.grid(row=4, column=3)

    Label(window, text="e-mail").grid(row=5, column=0)
    emailEntry = Entry(window, fg="yellow", bg="blue", width=20)
    emailEntry.grid(row=5, column=1)

    Label(window, text="nr telefonu").grid(row=5, column=2)
    telEntry = Entry(window, fg="yellow", bg="blue", width=12)
    telEntry.grid(row=5, column=3)


    Button(window,
           text="Rejestracja",
           bg="blue",
           fg="yellow",
           command=register,
           ).grid(row=7, column=0, pady=10)

    # side = LEFT / RIGHT
    # .pack(pady)

    window.mainloop()

# -------------------- client panel --------------------#


def PanelKlienta():
    # user
    clear()
    global user
    Label(window, text="Użytkownik:%s" % (user.login)).grid(row=0, column=0)
    Button(window,
           text="Lista Produktów",
           bg="blue",
           fg="yellow",
           command=ProductsList,
           width=15,
           ).grid(row=1, column=0, pady=10)

    Button(window,
           text="Konto",
           bg="blue",
           fg="yellow",
           command=Account,
           width=15,
           ).grid(row=1, column=1)

    Button(window,
           text="Koszyk",
           bg="blue",
           fg="yellow",
           command=CartList,
           width=15,
           ).grid(row=1, column=2)
    # window.mainloop()


# -------------------- products list --------------------#

def ProductsList():
    clear()
    PanelKlienta()
    strona = search.przegladanie()
    x=3

    
    def Search():
        searchResults = search.wyszukaj(searchInput.get())
        clear()
        PanelKlienta()
        b=2
        for x in searchResults:
            Label(window, text=f"{x.name}").grid(row=b,column=0)
            Label(window, text=f"{x.price}").grid(row=b,column=1)
            print(x.name, x.price)
            b+=1

    def AddToCart(prod):
        print(prod)
        
    Label(window, text="Wyszukaj: ").grid(row=2, column=0)
    searchInput = Entry(window, width=8)
    searchInput.grid(row=2, column=1)
    Button(window,
           text="Lista Produktów",
           bg="blue",
           fg="yellow",
           command=Search,
           width=15,
           ).grid(row=2, column=2, pady=10)

    for prod in strona:
        Label(window, text=f"{prod.name}").grid(row=x, column=0)
        # .grid(row=x, column=0)
        Label(window, text=f"{round(prod.price, 2)}").grid(row=x, column=1)
        Button(window, text="Dodaj do koszyka", command=lambda:AddToCart(prod.name)).grid(row=x, column=2)
        # self.listaProduktow[x].wyswietl()
        x+=1

# -------------------- account --------------------#

def Account():
    clear
    PanelKlienta()

    Button(window,
           text="Dane",
           bg="blue",
           fg="yellow",
           command=AccountData,
           width=15,
           ).grid(row=2, column=0)


    Button(window,
           text="Zamowienia",
           bg="blue",
           fg="yellow",
           command=Orders,
           width=15,
           ).grid(row=2, column=1)


def AccountData():
    clear
    PanelKlienta()
    
    user.wypiszDane()

    Label(window,
        text=f"Imie: {user.daneOsobowe(user.login)[0]}"
        ).grid(row=3, column=0) # .grid(row=x, column=0)

    Label(window,
        text=f"Nazwisko: {user.daneOsobowe(user.login)[1]}"
        ).grid(row=3, column=1)

    Label(window,
        text=f"Ulica: {user.daneKontaktowe(user.login)[3]}"
        ).grid(row=4, column=0)

    Label(window,
        text=f"Nr mieszkania: {user.daneKontaktowe(user.login)[4]}"
        ).grid(row=4, column=1)

    Label(window,
        text=f"Kod Pocztowy: {user.daneKontaktowe(user.login)[5]}"
        ).grid(row=5, column=0)

    Label(window,
        text=f"Miasto: {user.daneKontaktowe(user.login)[2]}"
        ).grid(row=5, column=1)

    Label(window,
        text=f"Email: {user.daneKontaktowe(user.login)[0]}"
        ).grid(row=6, column=0)

    Label(window,
        text=f"Nr Telefonu: {user.daneKontaktowe(user.login)[1]}"
        ).grid(row=6, column=1)

def Orders():
    clear
    PanelKlienta()

    print("Zrobić zamówienia")
    Label(window,
        text=f"Brak zamówień"
        ).grid(row=3, column=0)


# -------------------- cart --------------------#

def CartList():
    clear
    PanelKlienta()
    
    myCart = cart.pokazZawartosc()
    cartUpdate =[]
    x=2
    for prod in myCart:                  
        cartName = Label(window,
                    text=f"{prod.produkt.name}")  # .grid(row=x, column=0)
        cartName.grid(row=x, column=0)

        cartPrice = Label(window,
                    text="%.2fzł" % round(prod.produkt.price, 2))  # .grid(row=x, column=0)
        cartPrice.grid(row=x, column=1)

        cartNumber = Entry(window, width=8)
        cartNumber.insert(0, f"{prod.ilosc}")
        cartNumber.grid(row=x, column=2)
        cartUpdate.append((cartName,cartNumber))
        x+=1


    endPrice = Label(window,
                text=f"Suma: {cart.obliczWartosc()}")  # .grid(row=x, column=0)
    endPrice.grid(row=x, column=2)

    Button(window,
           text="Zapisz",
           bg="blue",
           fg="yellow",
           command=lambda:CartEdit(cartUpdate),
           width=7,
           ).grid(row=x+1, column=2, sticky=W)

    Button(window,
           text="Anuluj",
           bg="blue",
           fg="yellow",
           command=CartList,
           width=7,
           ).grid(row=x+1, column=2, sticky=E)

def CartEdit(update):
    global cart
    for x in update:
        for prod in Produkty:
            if prod.name == x[0]['text']:
                cart.zmien(prod,x[1].get())
                #print(x[0]['text'],x[1].get())
    CartList()


# -------------------- orders --------------------#




# ----------------------------------- MAIN -----------------------------------#

def main():

    GoscGUI()

if __name__ == '__main__':
    main()
