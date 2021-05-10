--select product, price from items where price >= 80 order by price desc;
--select first_name, last_name from customers order by first_name asc fetch first 3 row only; 
select last_name from customers order by last_name desc;

--create table purchases(
--id serial,
--customer_id integer,
--item_id integer,
--primary key (id),
--foreign key (customer_id) references customers (customer_id),
--foreign key (item_id) references items (item_id)
--);

--insert into purchases(customer_id, item_id)
--values (001, null);

--insert into purchases (customer_id, item_id)
--values (2, 3),
--(1, 2),
--(4, 1),
--(5, 2),
--(3, 1);

--select * from purchases

--select purchases.item_id, purchases.customer_id
--from purchases
--inner join customers
--on purchases.customer_id = customers.customer_id;

--SELECT * FROM purchases INNER JOIN customers ON purchases.customer_id = customers.customer_id WHERE customers.customer_id = 4;


--select customer_id from purchases where item_id = 1 or item_id = 2;
--select * from purchases inner join items on purchases.item_id = items.item_id where items.product = 'Small_Desk' or items.item_id=2;

--insert into items(product, price)
--values('hard drive', 50);

--select customers.first_name, customers.last_name, items.product
--from customers inner join items on customers.customer_id = items.item_id;











