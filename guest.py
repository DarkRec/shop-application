from connection import *
from client import *
from db import *
from admin import *


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
        DB.AddClient(login, imie, nazwisko, email,
                     miasto, ulica, lokal, kod, nrTel)
        DB.AddUser(login, haslo)

    def logowanie(login, haslo):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT type FROM users WHERE username = '%s' AND password LIKE '%s'" % (login, haslo))
        fetchedRow = cursor.fetchone()
        try:
            global user
            if fetchedRow[0] == 'user':
                user = Klient(login)
                global cart
                cart = Koszyk(login)
                print('Logowanie użytkownika ', login)
                return user
            elif fetchedRow[0] == 'admin':
                print('Logowanie administratora', login)
                user = Admin(login)
                return user
        except:
            print("Błąd logowania")
            return 'guest'


user = Gosc()
