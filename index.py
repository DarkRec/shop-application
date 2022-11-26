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


# ----------------------------------- MAIN -----------------------------------#

def donothing():
    print("a")


def main():
    root = Tk()
    gui = GUI(root)

    #menubar = Menu(root)
    #menubar.add_cascade(label="File", command=donothing)

    # root.config(menu=menubar)

    root.mainloop()


if __name__ == '__main__':
    main()
