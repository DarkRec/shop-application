#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from DB import DB
from tkinter import messagebox
from typing import List

from security.passwd import *
from DB import *
from Klient import *
from Koszyk import *

from connection import *
cursor = connection.cursor()


class Gosc:
    def logowanie(login, passwd) -> str:  # Klient_Admin
        type = DB.SelectUser(login)
        try:
            #print(verify_password(passwd, type[0]))
            if verify_password(passwd, type[0]):
                return type[1]
        finally:
            pass

    def rejestracja(login, passwd, imie, nazwisko, email, miasto, ulica, nr_mieszkania, kod_pocztowy, nr_telefonu) -> None:
        usr = DB.SelectUser(login)

        # print(usr)
        if usr is not None:
            messagebox.showerror(
                "Register Error", "Taki użytkownik już istnieje")
            # print(usr)
        else:
            DB.AddClient(login, imie, nazwisko, email,
                         miasto, ulica, nr_mieszkania, kod_pocztowy, nr_telefonu)
            DB.AddUser(login, get_password_hash(passwd))

    def __init__(self):
        self._datastore: DB = None
        self.type = 'guest'
