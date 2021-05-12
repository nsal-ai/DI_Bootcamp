--select * from language

--select film.title, film.description, language.language_id
--from film
--inner join language
--on film.language_id = language.language_id

create table new_film(
new_film_id serial primary key,
id integer,
name varchar (80)
);

insert into new_film (id, name)
values (1, 'independence day'), (2, 'inception'), (3, 'matrix'), (4, 'breakfast club'), (5, 'heat')



insert into customer_review(review_id, film_id, language_id, title, score, review_text, last_update)
values (1, 1, 1, 'independence day', 7, 'an easy watch with some great one-liners. A must watch for alien enthusiasts', '11/05/2021'),
(2, 4, 1, 'breakfast club', 9, 'an all-time classic feel good movie that houses some great names. A film that can be enjoyed throughout the ages', '11/05/2021')

select * from customer_review

select * from new_film

delete from new_film
where id = 1
returning *;

drop table customer_review;

create table customer_review(
review_id serial,
film_id integer,
language_id integer,
title varchar (50),
score integer,
review_text varchar,
last_update date,
primary key (review_id),
foreign key (film_id) references new_film(new_film_id) on delete cascade

);

select * from customer_review

drop table customer_review;

select film.title, film.language_id from film where language_id = 2;

update film
set language_id = 2 where title = 'Chamber Italian';


select film.title, film.film_id, film.rental_rate, rental.return_date from film
inner join rental
on film.film_id = rental.inventory_id
where return_date is null order by rental_rate desc;

select film.title, film.film_id, film.rental_rate, rental.return_date from film
inner join rental
on film.film_id = rental.inventory_id
where return_date is null order by rental_rate desc;

select film.title, film.description, actor.first_name, actor.last_name from film
inner join actor
on film.film_id = actor.actor_id
where actor.first_name = 'Penelope' and actor.last_name = 'Monroe';


select film.title, film.length, film.rating, film_category.film_id from film
inner join film_category
on film.film_id = film_category.film_id
where film.length < 60 and film.rating = 'R'
and description like '%Documentary%';

select film.title, customer.first_name, customer.last_name, payment.amount, rental.return_date
from rental 
inner join customer
on rental.customer_id = customer.customer_id -- 
inner join payment
on rental.rental_id = payment.rental_id 
inner join inventory
on rental.inventory_id = inventory.inventory_id 
inner join film 
on inventory.film_id = film.film_id
where customer.first_name = 'Matthew'
and customer.last_name = 'Mahan'
and rental.return_date < '2005-08-01'
and rental.return_date > '2005-07-28'
and payment.amount > 4

select film.title, film.description, customer.first_name, customer.last_name, payment.amount, payment.payment_id, film.replacement_cost, inventory.inventory_id
from rental
inner join customer
on rental.customer_id = customer.customer_id
inner join payment
on rental.rental_id = payment.rental_id
inner join inventory
on rental.inventory_id = inventory.inventory_id
inner join film
on inventory.film_id = film.film_id
where customer.first_name = 'Matthew'
and customer.last_name = 'Mahan'
and (title like '%Boat%' or description like '%Boat%')
order by replacement_cost desc


