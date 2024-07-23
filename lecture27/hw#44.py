"""
1. Install SQLite
2. Create table Persons(name: string, favorite_color: string, profit: float)
3. Create table Cars(model: string, color: string, price: float)
4. Fill in tables with data:
Data in table Persons:
name text,
favorite_color text,
profit float
Data in table Cars:
model text,
color text,
price float
5. For every person who can afford to buy a car, print the cheapest car of his favorite color
(car price should be less or equal to person's profit)
Order result by person's name in alphabetical order ascending.
6. (*optional) For every person, print the cheapest car of his favorite color. If person can't
afford a car, print NULL for columns model and price.
Order result by person's name in alphabetical order ascending.
Attach .sql file with all queries (tables creation, inserting data, selecting data)
"""
import sqlite3


def create_tables():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query_persons = """ CREATE TABLE IF NOT EXISTS Persons(name text, favorite_color text, profit float); """
        with open('db/requests.sql', 'a') as file:
            file.write(f'{query_persons}\n\n')
        cursor.execute(query_persons)
        cursor.close()

    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query_cars = """ CREATE TABLE IF NOT EXISTS Cars(model text, color text, price float); """
        with open('db/requests.sql', 'a') as file:
            file.write(f'{query_cars}\n\n')
        cursor.execute(query_cars)
        cursor.close()

    return 'Tables created successfully!'


def fill_tables():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query_persons = """ INSERT INTO Persons(name, favorite_color, profit)
                    VALUES('John', 'red', 1000), ('Anna', 'red', 2000),
                    ('James', 'green', 500), ('Karl', 'black', 2500); """
        with open('db/requests.sql', 'a') as file:
            file.write(f'{query_persons}\n\n')
        cursor.execute(query_persons)
        cursor.close()

    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query_cars = """ INSERT INTO Cars(model, color, price)
                    VALUES('BMW M1', 'blue', 700), ('BMW M2', 'black', 1700), ('BMW M3', 'black', 2300),
                    ('Fiat M1', 'red', 1500), ('Fiat M2', 'red', 1000), ('Chevrolet M1', 'green', 501); """
        with open('db/requests.sql', 'a') as file:
            file.write(f'{query_cars}\n\n')
        cursor.execute(query_cars)
        cursor.close()

    return 'Tables filled successfully!'


def select_data():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT Persons.name, Cars.model, Cars.color, Cars.price, Persons.profit
                    FROM Persons INNER JOIN Cars ON Persons.profit >= Cars.price
                    AND Persons.favorite_color = Cars.color Group by Persons.name having min(Cars.price); """
        with open('db/requests.sql', 'a') as file:
            file.write(f'{query}\n\n')
        cursor.execute(query)
        cursor.close()

    return 'Data selected successfully!'


def select_data_optional():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT Persons.name, Cars.model, Persons.favorite_color, Cars.price, Persons.profit
                    FROM Persons LEFT JOIN Cars ON Persons.favorite_color = Cars.color 
                    and Persons.profit >= Cars.price
                    Group by Persons.name having min(Cars.price) is null or min(Cars.price) is not null; """
        with open('db/requests.sql', 'a') as file:
            file.write(f'{query}\n\n')
        cursor.execute(query)
        cursor.close()

    return 'Data selected successfully!'


print(create_tables())
print(fill_tables())
print(select_data())
print(select_data_optional())




