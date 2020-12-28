drop table if exists employee;

create table employee (
	employee_id int,
	name varchar,
	months int,
	salary int
);

select name
from employee
order by name asc;

alter schema employee_names
rename to employees;

select name
from employee
where (salary > 2000) and (months < 10);