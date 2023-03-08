# Shop application

Window application for shop (dedicated is paper shop)

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Features](#features)

## General info

Application for internet paper shop. Firstly created as a final project for studies in the subject of Programming designing.

![obraz](https://user-images.githubusercontent.com/54840416/223776718-5c114136-0bd6-46e1-93a0-cda823cac218.png)

## Technologies

- Python v.3.11.1
- pip v23.0.1
- mySQL database

## Setup

To run this project first install libraries using pip

```
$ pip install -r requirements.txt
```

then run program using

```
$ python main.py
```

### Database

To connect to the database, change file /DB/connection.py

```
(database='DB_name',
 host="host",
 user="DB_username",
 password="DB_password")
```

## Features

### 3 different user interfaces, for:

- Guests
- Registered users
- Administrators

### Interface

- Products List / Info
- Searching by name / category
- Login / Register
- Orders List / Info

### Hashing password
