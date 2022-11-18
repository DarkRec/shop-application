from connection import *
from client import *
from db import *


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
        DB.AddClient(login, imie, nazwisko, email, miasto, ulica, lokal, kod, nrTel)
        DB.AddUser(login, haslo)

    def logowanie(login, haslo):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT type FROM users WHERE username = '%s' AND password LIKE '%s'" % (login, haslo))
        fetchedRow = cursor.fetchone()
        try:
            if fetchedRow[0] == 'user':
                global user
                user = Klient(login, fetchedRow[0])
                global cart
                cart = Koszyk(login)
                print('Logowanie użytkownika ', login)
                return user
            elif fetchedRow[0] == 'admin':
                print('Logowanie administratora', login)
                return 'admin'
        except:
            print("Błąd logowania")
            return 'guest'


user = Gosc()
