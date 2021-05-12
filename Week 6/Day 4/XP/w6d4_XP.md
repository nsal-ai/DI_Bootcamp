select first_name, last_name as Last_Name from employees;

select employee_id from employees

select * from employees order by first_name desc

select * from employees

select first_name, last_name, salary, 0.15*salary as PF from employees;

select employee_id, first_name, last_name, salary from employees order by salary asc;

select sum(salary) as Total_Salary_Paid from employees;

select max(salary), min(salary) from employees;

select avg(salary) from employees;

select left(first_name, 3) from employees;

select * from employees order by salary desc
limit 10

select first_name, last_name, salary from employees
where salary >= 10000 and salary <= 15000


select last_name, salary, jobs.job_title from employees
inner join jobs
on employees.job_id = jobs.job_id
where jobs.job_title != 'Programmer' 
and jobs.job_title != 'Shipping Clerk'
and employees.salary != 4500
and employees.salary != 10000
and employees.salary != 15000

select last_name from employees
where substring(last_name, 3,1) = 'e';

select * from employees
where last_name = 'Jones' 
or last_name = 'Scott'
or last_name = 'King'
or last_name = 'Ford'

