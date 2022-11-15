from tkinter import *
from asyncio.windows_events import NULL

from connection import *
from guest import *
from client import *
from cart import *
from product import *
from show import *
from orders import *
from gui import *


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


# ----------------------------------- MAIN -----------------------------------#

# def main():


# if __name__ == '__main__':
#    main()
