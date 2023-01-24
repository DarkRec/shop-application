#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import messagebox

from security.passwd import *
from app.DB import *


class Gosc:
    def logowanie(login, passwd) -> str:
        type = DB.SelectUser(login)
        try:
            if verify_password(passwd, type[0]):
                return type[1]
        finally:
            pass

    def rejestracja(self, login, passwd, imie, nazwisko, email, miasto, ulica, nr_mieszkania, kod_pocztowy, nr_telefonu) -> None:
        usr = DB.SelectUser(login)
        if usr is not None:
            messagebox.showerror(
                "Register Error", "Taki użytkownik już istnieje")
        else:
            DB.AddClient(login, imie, nazwisko, email,
                         miasto, ulica, nr_mieszkania, kod_pocztowy, nr_telefonu)
            DB.AddUser(login, get_password_hash(passwd))
            #self.logowanie(login, passwd)

    def __init__(self):
        self.type = 'guest'
