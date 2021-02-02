drop table if exists employees;

create table employees (
	id integer,
	name varchar,
	salary integer
);

--Query the Difference Between the Average Actual & Average Miscalculated Salary
select cast(ceiling(avg(cast(salary as float)) - avg(cast(replace(cast(salary as varchar), '0', '') as float))) as integer)
from employees;