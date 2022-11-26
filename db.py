from connection import *

cursor = connection.cursor()


class DB:

    def AddToCart(prod, username):
        cursor.execute(
            f"INSERT INTO koszyk (`username`, `produkt`) VALUES ('{username}', '{prod}');")
        connection.commit()

    def RemoveFromCart(prod, username):
        cursor.execute(
            f"SELECT _id FROM `koszyk` WHERE (`username` = '{username}' AND `produkt` = '{prod}');")
        fetchedRows = cursor.fetchall()

        for x in fetchedRows:
            connection.cursor().execute(
                f"DELETE FROM `koszyk` WHERE (`_id` = '{x[0]}');")
            connection.commit()

    def ProdInCart(prod):
        cursor.execute(
            f"SELECT COUNT(*) FROM sklep.koszyk WHERE produkt = '{prod}';")
        return int(cursor.fetchone()[0])

    def UpdateClient(login, imie, nazwisko, email, nrTel, miasto, ulica, lokal, kod):
        connection.cursor().execute(
            f"UPDATE `klienci` SET `imie` = '{imie}', `nazwisko` = '{nazwisko}', `email` = '{email}', `nrTelefonu` = '{nrTel}', `miasto` = '{miasto}', `ulica` = '{ulica}', `lokal` = '{lokal}', `kodPocztowy` = '{kod}' WHERE (`username` = '{login}');")
        connection.commit()

    def FromCartToOrder(cart, login):
        for x in cart:
            try:
                cursor.execute(
                    f"SELECT ilosc FROM produkty WHERE _id = '{x.produkt.id}';")
                fetchedRow = cursor.fetchone()
                connection.cursor().execute(
                    f"UPDATE `produkty` SET `ilosc` = '{fetchedRow[0]-x.ilosc}' WHERE (`_id` = '{x.produkt.id}');")

                cursor.execute(
                    f"SELECT _id FROM `koszyk` WHERE (`username` = '{login}' AND `produkt` = '{x.produkt.name}');")
                fetchedRows = cursor.fetchall()
                for x in fetchedRows:
                    connection.cursor().execute(
                        f"DELETE FROM `koszyk` WHERE (`_id` = '{x[0]}');")
            finally:
                connection.commit()

    def AddUser(login, haslo):
        cursor.execute(
            f"INSERT INTO users (`username`, `password`) VALUES ('{login}', '{haslo}');")
        connection.commit()

    def AddClient(login, imie, nazwisko, email, miasto, ulica, lokal, kod, nrTel):
        cursor.execute("INSERT INTO klienci (`username`, `imie`, `nazwisko`, `email`, `miasto`, `ulica`, `lokal`, `kodPocztowy`, nrTelefonu) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
            login, imie, nazwisko, email, miasto, ulica, lokal, kod, nrTel))
        connection.commit()

    def AddProduct(nazwa, cena, ilosc, opis):
        cursor.execute(
            f"INSERT INTO produkty (`nazwa`, `cena`, `ilosc`, `opis`) VALUES ('{nazwa}', '{cena}', '{ilosc}', '{opis}');")
        connection.commit()

    def AddOrder(login, klient, wartosc, lista, data):
        cursor.execute(
            f"INSERT INTO zamowienia (`username`, `dane`, `wartosc` , `lista`, `utworzenie`) VALUES ('{login}', '{klient}', '{wartosc}', '{lista}', '{data}');")
        connection.commit()

    def loadOrders(login):
        cursor.execute(
            f"SELECT wartosc, utworzenie, stan FROM zamowienia WHERE username = '{login}';")
        return cursor.fetchall()

    def editCartProdNum(prod, ilosc, login):
        cursor.execute(
            f"SELECT ilosc FROM produkty WHERE nazwa = '{prod}';")
        fetchedRow = cursor.fetchone()
        if int(ilosc) > int(fetchedRow[0]):
            ilosc = int(fetchedRow[0])
        connection.cursor().execute(
            f"UPDATE `koszyk` SET `ilosc` = '{ilosc}' WHERE (`username` = '{login}' AND `produkt` = '{prod}');")
        connection.commit()

    def RemoveProduct(prodName):
        cursor.execute(
            f"SELECT _id FROM produkty WHERE nazwa = '{prodName}';")
        fetchedRow = cursor.fetchone()

        connection.cursor().execute(
            f"DELETE FROM `produkty` WHERE (`_id` = '{fetchedRow[0]}');")
        connection.commit()

        cursor.execute(
            f"SELECT _id FROM `koszyk` WHERE (`produkt` = '{prodName}');")
        fetchedRows = cursor.fetchall()

        for x in fetchedRows:
            connection.cursor().execute(
                f"DELETE FROM `koszyk` WHERE (`_id` = '{x[0]}');")
        connection.commit()
