CREATE TABLE students(
students_id SERIAL PRIMARY KEY,
last_name VARCHAR (50),
first_name VARCHAR (50),
birth_date DATE NOT NULL
);


INSERT INTO students (last_name, first_name, birth_date)
VALUES ('Benichou', 'Marc', '02/11/1998');
       ('Cohen', 'Yoan', '03/12/2010'),
	   ('Benichou', 'Lea', '27/07/1987'),
	   ('Dux', 'Amelia', '07/04/1996'),
	   ('Grez', 'David', '14/06/2003'),
	   ('Simpson', 'Omer', '03/10/1980')

the dates are presented in YYYY/MM/DD format

most efficient way to enter data according to postgreSQL is using the COPY method

SELECT * FROM students
SELECT first_name, last_name FROM students;
SELECT first_name, last_name FROM students WHERE students_id = 2;
SELECT first_name, last_name FROM students WHERE first_name = 'Marc' and last_name = 'Benichou';
SELECT first_name, last_name FROM students WHERE first_name = 'Marc' or last_name = 'Benichou';
SELECT first_name, last_name, birth_date FROM students WHERE first_name LIKE '%a%';
SELECT first_name, last_name, birth_date FROM students WHERE first_name LIKE 'a%';
SELECT first_name, last_name, birth_date FROM students WHERE LEFT(RIGHT(first_name,2),1) = 'a';
SELECT first_name, last_name, birth_date FROM students WHERE students_id = 1 or students_id = 3;
SELECT * FROM students WHERE birth_date >= '01/01/2000';