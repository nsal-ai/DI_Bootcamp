CREATE TABLE items(
 item_id SERIAL PRIMARY KEY,
 product VARCHAR (50),
 price SMALLINT NOT NULL
);

CREATE TABLE customers(
 customer_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50),
 last_name VARCHAR (50)
);

INSERT INTO items(product, price)
VALUES ('Small_Desk', 100),
	   ('Large_Desk', 300),
	   ('Fan', 80)
	   
INSERT INTO customers(first_name, last_name)
VALUES ('Greg', 'Jones'),
       ('Sandra', 'Jones'),
	   ('Scott', 'Scott'),
	   ('Trevor', 'Green'),
	   ('Melanie', 'Johnson')


SELECT * FROM items;      
SELECT product FROM items WHERE price > 80;
SELECT product, price FROM items WHERE price > 80;
SELECT product, price FROM items WHERE price < 300;

for values that do not exist, when selected from table will return the empty columns

SELECT first_name, last_name FROM customers WHERE last_name = 'Jones';

SELECT first_name, last_name FROM customers WHERE first_name != 'Scott';