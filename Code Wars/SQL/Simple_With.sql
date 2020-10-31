with special_sales as (
select distinct departments.id, departments.name
from departments
	join sales
	on departments.id = sales.department_id
where price in (
  select price
  from sales
	where price > 90.00 
))
select *
from special_sales
order by id asc;

drop table if exists departments;
drop table if exists sales;

create table if not exists departments (
	id integer primary key,
	name varchar
);
create table if not exists sales (
	id integer primary key,
	department_id integer,
	name varchar,
	price decimal,
	card_name varchar,
	card_number bigint,
	transaction_date date,
	constraint dept_id
		foreign key (department_id) references departments(id)
);

select *
from departments;

select *
from sales;