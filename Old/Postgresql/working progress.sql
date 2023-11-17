select version();

select * from movies;

insert into movies(id, movie, rating) 
values(1,'jailer',9), (2, 'vikram', 8), (3, 'leo', 7);

insert into movies(id, movie, rating) 
values(4, 'sura',5), (5, 'agan', 6), (6, 'deena', 8.5), (7, 'master', 8),
(8, 'kala', 7)

select * from movies 
where rating > 8;

alter table movies
rename column rating to ratings;

select * from movies
where avg(ratings);

select * from movies order by ratings desc;

select avg(salary) from employees

select max(salary) from employees

select min(salary) from employees

select count(distinct country) from employees

update movies 
set    ratings = 7
where  ratings=5;


create table employees(emp_id int, name varchar(100), 
					   gender varchar(10), department varchar(30), 
					   country varchar(30), salary real)

select distinct country from employees


select * from employees order by salary desc limit(3) offset(23)

select * from employees 
where  name like '%e__'



select country, count(emp_id) from employees 
group by country having count(emp_id) < 25






select country, department, salary,
case
when salary > 10000 and salary < 60000
then 'low salary'
when salary >60000 and salary < 80000
then 'Medium salary'
when salary > 80000
then 'high salary'
end as salary_category
from employees
order by salary limit (120)


select name,department, country, salary from employees
where salary > (select avg(salary) from employees)


create or replace function
count_country()
returns integer as $total_countrys$
declare 
	total_country integer;
begin
	select count(country) into total_country
	from employees;
	return total_country;
end;
$total_countrys$ language plpgsql;

select count_country();






