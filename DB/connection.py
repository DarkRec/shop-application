import mysql.connector

connection = mysql.connector.connect(
    database='DB_name',
    host="host",
    user="DB_username",
    password="DB_password"
)
