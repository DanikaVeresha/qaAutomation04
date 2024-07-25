 CREATE TABLE IF NOT EXISTS Persons(
 name text, favorite_color text, profit float);

 CREATE TABLE IF NOT EXISTS Cars(
 model text, color text, price float);

 INSERT INTO Persons(name, favorite_color, profit)
                    VALUES('John', 'red', 1000), ('Anna', 'red', 2000),
                    ('James', 'green', 500), ('Karl', 'black', 2500);

 INSERT INTO Cars(model, color, price)
                    VALUES('BMW M1', 'blue', 700), ('BMW M2', 'black', 1700), ('BMW M3', 'black', 2300),
                    ('Fiat M1', 'red', 1500), ('Fiat M2', 'red', 1000), ('Chevrolet M1', 'green', 501);

 SELECT Persons.name, Cars.model, Cars.color, Cars.price, Persons.profit
                    FROM Persons INNER JOIN Cars ON Persons.profit >= Cars.price
                    AND Persons.favorite_color = Cars.color Group by Persons.name having min(Cars.price);

 SELECT Persons.name, Cars.model, Persons.favorite_color, Cars.price, Persons.profit
                    FROM Persons LEFT JOIN Cars ON Persons.favorite_color = Cars.color
                    and Persons.profit >= Cars.price
                    Group by Persons.name having min(Cars.price) is null or min(Cars.price) is not null;