import sqlite3 as sql3
import sqlalchemy as alch
from sqlalchemy import sql

connection = sql3.connect('sneakers.db')

with connection:
    connection.execute("""
        DROP TABLE SNEAKERSN1
    """)
    connection.execute("""
        CREATE TABLE SNEAKERSN1 (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            count INTEGER,
            manufacture TEXT,
            price FLOAT,
            size FLOAT
        );
    """)

engine = alch.create_engine('sqlite:///sneakers.db')
engine.connect()

while True:
    print('Ваш запрос?\n'
          'add - добавление\n'
          'show me all - отображение всего\n'
          'delete smth - удалить позицию\n'
          'position stats - статистика по позициям\n')
    command = input()
    if command == 'add':
        print('Задать название кроссовок:')
        Name: str = input()
        print('Задать колличество кроссовок:')
        Count = int(input())
        print('Задать производителя производителя:')
        Manufacture = input()
        print('Задать цену:')
        Price = float(input())
        print('Задать размер:')
        Size = float(input())

        alch = 'INSERT INTO SNEAKERSN1 (name, count, manufacture, price, size) values(?, ?, ?, ?, ?)'
        data = [
            (Name, Count, Manufacture, Price, Size)
        ]

        with connection:
            connection.executemany(sql, data)
            data = connection.execute("SELECT * FROM SNEAKERSN1")
            for row in data:
                print(row)

    elif command == 'show me all':
        with connection:
            data = connection.execute("SELECT * FROM SNEAKERSN1")
            for row in data:
                print(row)

    elif command == 'delete smth':
        print('Задать id для удаления:')
        position_for_delete = input()
        str = "DELETE FROM SNEAKERS1 WHERE ID=" + position_for_delete
        with connection:
            data = connection.execute(str)

    elif command == 'position stats':
        with connection:
            data = connection.execute("SELECT COUNT(id) FROM SNEAKERSN1")
            for row in data:
                print(row[0])
