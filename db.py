#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import Produkt
import GUI
from typing import List

from connection import *
cursor = connection.cursor()


# cursor.execute(f"")
# fetchedRows = cursor.fetchall()
# cursor.fetchone()
# connection.commit()

class DB:
    def AddClient(login: str, imie: str, nazwisko, email: str,
                  miasto: str, ulica: str, nr_mieszkania: str, kod_pocztowy: str, nr_telefonu: str) -> None:
        cursor.execute(
            f"INSERT INTO `klienci` (`login`, `imie`, `nazwisko`, `ulica`, `nr_mieszkania`, `kod_pocztowy`, `miasto`, `email`, `nr_telefonu`) VALUES ('{login}', '{imie}', '{nazwisko}', '{ulica}', '{nr_mieszkania}', '{kod_pocztowy}', '{miasto}', '{email}', '{nr_telefonu}');")
        connection.commit()

    def AddUser(login: str, hashed_passwd: str) -> None:
        cursor.execute(
            f"INSERT INTO `users` (`username`, `password`) VALUES ('{login}', '{hashed_passwd}');")
        connection.commit()

    def SelectUser(login: str) -> str:
        cursor.execute(
            f"SELECT password, type FROM `users` WHERE username = '{login}'")
        return cursor.fetchone()

    def UpdateClient(login: str, imie: str, nazwisko: str, email: str, nrTel: str, miasto: str, ulica: str, lokal: str, kod: str) -> None:
        connection.cursor().execute(
            f"UPDATE `klienci` SET `imie` = '{imie}', `nazwisko` = '{nazwisko}', `email` = '{email}', `nr_telefonu` = '{nrTel}', `miasto` = '{miasto}', `ulica` = '{ulica}', `nr_mieszkania` = '{lokal}', `kod_pocztowy` = '{kod}' WHERE (`login` = '{login}');")
        connection.commit()

    def AddToCart(prodID: int, username: str) -> None:
        cursor.execute(
            f"INSERT INTO koszyk (`username`, `produktID`) VALUES ('{username}', '{prodID}');")
        connection.commit()

    def RemoveFromCart(prodID: int, username: str) -> None:
        cursor.execute(
            f"DELETE FROM `koszyk` WHERE (`username` = '{username}' AND `produktID` = '{prodID}');")
        connection.commit()
        # fetchedRows = cursor.fetchall()
        # for x in fetchedRows:
        #    connection.cursor().execute(
        #        f"DELETE FROM `koszyk` WHERE (`_id` = '{x[0]}');")

    def ProductInCart(prod: int) -> int:
        cursor.execute(
            f"SELECT COUNT(*) FROM koszyk WHERE produktID = '{prod}';")
        return int(cursor.fetchone()[0])

    def ClientCart(username: str) -> str:
        cursor.execute(
            f"SELECT produkty._id, produkty.nazwa, produkty.cena, produkty.ilosc, produkty.opis, produkty.kategoria, koszyk.ilosc FROM koszyk INNER JOIN produkty ON koszyk.produktID = produkty._id WHERE username = '{username}';")
        return cursor.fetchall()

    def EditCartProductNumber(prod: str, ilosc: int, login: str) -> None:
        cursor.execute(
            f"SELECT _id, ilosc FROM produkty WHERE nazwa = '{prod}';")
        fetchedRow = cursor.fetchone()
        if int(ilosc) > int(fetchedRow[1]):
            ilosc = int(fetchedRow[1])
        connection.cursor().execute(
            f"UPDATE `koszyk` SET `ilosc` = '{ilosc}' WHERE (`username` = '{login}' AND `produktID` = '{int(fetchedRow[0])}');")
        connection.commit()

    def FromCartToOrder(cart, login) -> None:
        for x in cart:
            try:
                cursor.execute(
                    f"SELECT ilosc FROM produkty WHERE _id = '{x.produkt.id}';")
                fetchedRow = cursor.fetchone()
                connection.cursor().execute(
                    f"UPDATE `produkty` SET `ilosc` = '{fetchedRow[0]-x.ilosc}' WHERE (`_id` = '{x.produkt.id}');")

                cursor.execute(
                    f"SELECT _id FROM `koszyk` WHERE (`username` = '{login}' AND `produktID` = '{x.produkt.id}');")
                fetchedRows = cursor.fetchall()
                for x in fetchedRows:
                    connection.cursor().execute(
                        f"DELETE FROM `koszyk` WHERE (`_id` = '{x[0]}');")
            finally:
                connection.commit()

    def AddOrder(login: str, klient: str, wartosc: float, lista: str, data, status: str) -> None:
        cursor.execute(
            f"INSERT INTO `zamowienia` (`username`, `dane`, `wartosc` , `lista`, `utworzenie`, `status`) VALUES ('{login}', '{klient}', '{wartosc}', '{lista}', '{data}', '{status}');")
        connection.commit()

    def loadUserOrders(login) -> None:
        cursor.execute(
            f"SELECT _id, wartosc, utworzenie, status FROM `zamowienia` WHERE username = '{login}';")
        return cursor.fetchall()

    def loadOrders() -> None:
        cursor.execute(
            f"SELECT _id, wartosc, utworzenie, status FROM `zamowienia`;")
        return cursor.fetchall()

    def AddProduct(nazwa: str, cena: float, ilosc: int, opis: str, kategoria: str) -> None:
        cursor.execute(
            f"SELECT * FROM `produkty` WHERE `nazwa` = '{nazwa}';")
        if cursor.fetchone() is None:
            cursor.execute(
                f"INSERT INTO produkty (`nazwa`, `cena`, `ilosc`, `opis`, `kategoria`) VALUES ('{nazwa}', '{cena}', '{ilosc}', '{opis}', '{kategoria}');")
            connection.commit()

    def ProductsList() -> str:
        cursor.execute("SELECT _id, nazwa, cena, ilosc, opis FROM produkty")
        return cursor.fetchall()

    def RemoveProduct(id: int) -> None:
        connection.cursor().execute(
            f"DELETE FROM `produkty` WHERE (`_id` = '{id}');")
        connection.commit()

    def SelectProduct(id: int) -> None:
        cursor.execute(
            f"SELECT nazwa, cena, ilosc, kategoria, opis FROM `produkty` WHERE `_id` = '{id}'")
        return cursor.fetchone()

    def EditProduct(id: int, nazwa: str, cena: float, ilosc: int, opis: str, kategoria: str) -> None:
        connection.cursor().execute(
            f"UPDATE `produkty` SET `nazwa` = '{nazwa}', `cena` = '{cena}', `ilosc` = '{ilosc}', `opis` = '{opis}', `kategoria` = '{kategoria}' WHERE (`_id` = '{id}');")
        connection.commit()

    def UserData(login: str) -> str:
        cursor.execute(
            f"SELECT `login`, `imie`, `nazwisko`, `ulica`, `nr_mieszkania`, `kod_pocztowy`, `miasto`, `email`, `nr_telefonu` FROM `klienci` WHERE login = '{login}';")
        return cursor.fetchone()

    def OrdersToAuthorization(self) -> None:
        pass

    def Authorization(id) -> None:
        connection.cursor().execute(
            f"UPDATE `zamowienia` SET `status` = 'in progress' WHERE (`_id` = '{id}');")
        connection.commit()

    def OrderInfo(id) -> None:
        cursor.execute(
            f"SELECT `dane`, `wartosc`, `lista`, `status`, `utworzenie` FROM `zamowienia` WHERE _id = '{id}';")
        return cursor.fetchone()

    def CancelOrder(id) -> None:
        connection.cursor().execute(
            f"UPDATE `zamowienia` SET `status` = 'canceled' WHERE (`_id` = '{id}');")
        connection.commit()

    def Paid(id: int, typ: str) -> None:
        connection.cursor().execute(
            f"UPDATE `zamowienia` SET `status` = 'waiting for authorization' WHERE (`_id` = '{id}');")
        cursor.execute(
            f"INSERT INTO `payment` (`orderID`, `type`) VALUES ('{id}', '{typ}');")
        connection.commit()

    def LoadDiscounts(self) -> None:
        pass

    def AddDiscount(self) -> None:
        pass

    def DeleteDiscount(self) -> None:
        pass

    def EditDiscount(self) -> None:
        pass

    def __init__(self):
        self._unnamed_GUI_: GUI = None


db = DB()
