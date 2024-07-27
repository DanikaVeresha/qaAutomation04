"""
Write a class to work with a database table.
The table must be created when the class is instantiated (during repeated instantiation, an
exception should not be thrown if the table already created).
The class must include the following methods:
 - to obtain all records as list of objects of user defined classes;
 - adding several records by passed objects into methods;
 - updating records by condition (choose condition by yourself)
 - obtaining records by condition (choose condition by yourself)
 - deleting records by condition (choose condition by yourself)
 - optionally add more methods/classes that will make working with the table easier
"""
import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_name, table_name, columns):
        self.db_name = db_name
        self.table_name = table_name
        self.columns = columns
        self._connection = None
        self._cursor = None
        self.create_table()

    def create_connection(self):
        """Create a database connection to a SQLite database"""
        try:
            self._connection = sqlite3.connect(self.db_name)
            self._cursor = self._connection.cursor()
        except Error as ex:
            print(f'Error: {ex} with database {self.db_name}')

    def create_table(self):
        """Create a table in the database if it does not exist"""
        self.create_connection()
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({self.columns})")
        self._connection.commit()

    def get_all_tables(self):
        """Get all tables from the database"""
        self.create_connection()
        self._cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self._cursor.fetchall()

    def get_all_records(self):
        """Get all records from the table"""
        self.create_connection()
        self._cursor.execute(f"SELECT * FROM {self.table_name}")
        return self._cursor.fetchall()

    def add_record(self, *records):
        """Add records to the table"""
        self.create_connection()
        for record in records:
            if isinstance(record, tuple):
                self._cursor.execute(f"INSERT INTO {self.table_name} VALUES {record}")
            elif isinstance(record, list):
                self._cursor.executemany(f"INSERT INTO {self.table_name} VALUES (?, ?, ?)", record)
        self._connection.commit()

    def update_record(self, new_values, *condition):
        """Update records by condition"""
        self.create_connection()
        for cond in condition:
            self._cursor.execute(f"UPDATE {self.table_name} SET {new_values} WHERE {cond}")
        self._connection.commit()

    def get_records_by_condition(self, condition):
        """Get records by condition"""
        self.create_connection()
        self._cursor.execute(f"SELECT * FROM {self.table_name} WHERE {condition}")
        return self._cursor.fetchall()

    def delete_records_by_condition(self, condition):
        """Delete records by condition"""
        self.create_connection()
        self._cursor.execute(f"DELETE FROM {self.table_name} WHERE {condition}")
        self._connection.commit()

    def drop_table(self):
        """Drop the table from the database"""
        self.create_connection()
        self._cursor.execute(f"DROP TABLE {self.table_name}")
        self._connection.commit()

    def close_connection(self):
        """Close connection to the database"""
        self._connection.close()

    def __del__(self):
        """Close connection to the database when the object is deleted"""
        self.close_connection()
        print(f'Connection to the database {self.db_name} with table {self.table_name} is closed')


# Example of usage
db_person = Database(
    'test_db',
    'Persons',
    'name TEXT, favorite_color TEXT, profit float'
)

db_car = Database(
    'test_db',
    'Cars',
    'model TEXT, color TEXT, price float'
)

db_person.add_record(
    ('John', 'red', 1000), ('Anna', 'red', 2000), ('James', 'green', 500), ('Karl', 'black', 2500)
)
db_car.add_record(
    [('BMW M1', 'blue', 700), ('BMW M2', 'black', 1700), ('BMW M3', 'black', 2300),
    ('Fiat M1', 'red', 1500), ('Fiat M2', 'red', 1000), ('Chevrolet M1', 'green', 501)]
)

print(f'Tables info -> \n{db_person.get_all_tables()}\n')
print(f'Persons info -> \n{db_person.get_all_records()}\n')
print(f'Cars info -> \n{db_car.get_all_records()}\n')

db_person.update_record('profit=1001', 'name="John"', 'name="James"')
db_car.update_record('price=800', 'model="BMW M1"', 'model="Fiat M2"')
print(f'Persons info after update data(profit=1001) -> \n{db_person.get_all_records()}\n')
print(f'Cars info after update data(price=800) -> \n{db_car.get_all_records()}\n')


print(f'Persons info where profit > 1000 -> \n{db_person.get_records_by_condition("profit >= 1000")}\n')
print(f'Cars info if where price > 1000 -> \n{db_car.get_records_by_condition("price > 1000")}\n')

db_person.delete_records_by_condition('profit < 2000')
db_car.delete_records_by_condition('price < 1000')
print(f'Persons info after delete data(profit < 2000) -> \n{db_person.get_all_records()}\n')
print(f'Cars info after delete data(price < 1000) -> \n{db_car.get_all_records()}\n')

db_person.drop_table()
print(f'Tables info after drop Persons table -> \n{db_person.get_all_tables()}\n')

db_user = Database(
    'user_db',
    'Users',
    'name TEXT, age INTEGER, address TEXT'
)
print(f'Tables info -> \n{db_user.get_all_tables()}\n')

db_user.add_record(
    ('John', 25, 'NY'), ('Anna', 30, 'LA'), ('James', 35, 'SF'), ('Karl', 40, 'CH')
)
print(f'Users info -> \n{db_user.get_all_records()}\n')

db_user.update_record('age=18', 'name="Anna"', 'name="James"')
print(f'Users info after update data(age=18) -> \n{db_user.get_all_records()}\n')

print(f'Users info where age=18 -> \n{db_user.get_records_by_condition("age = 18")}\n')

db_user.delete_records_by_condition('age <= 18')
print(f'Users info after delete data(age <= 18) -> \n{db_user.get_all_records()}\n')

db_user.drop_table()
print(f'Tables info after drop Users table -> \n{db_user.get_all_tables()}\n')



