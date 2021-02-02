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

--Write a Query to Find the Maximum Total Earnings for All Employees as Well as the Total Number of Employees Who Have Maximum Total Earnings
--Print These Values as Two Space Separated Integers
select top 1 max(months * salary) as total_earnings, '  ', count(*) as num_with_max
from employee
group by (months * salary)
order by total_earnings desc;