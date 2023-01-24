from tkinter import *
from asyncio.windows_events import NULL

import connection
#import app.Administrator
#import app.DB
#import app.ElementKoszyka
from GUI import *
#import app.Klient
#import app.Koszyk
#import app.Produkt
#import app.Przegladanie
#import app.Zamowienia
#import app.Zamowienie


# ----------------------------------- MAIN -----------------------------------#

def donothing():
    print("a")


# def main():

    # Resize the image using resize() method

    #menubar = Menu(root)
    #menubar.add_cascade(label="File", command=donothing)

    # root.config(menu=menubar)

if __name__ == '__main__':
    root = Tk()
    GUI(root)
    root.mainloop()
    # gui.PanelGoscia()
