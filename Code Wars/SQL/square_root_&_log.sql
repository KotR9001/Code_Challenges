drop table if exists decimals;

create table if not exists decimals (
	id int primary key, 
	number1 int, 
	number2 int
);

insert into decimals (id, number1, number2)
values (1, 4, 10), (2, 25, 1000), (3, 81, 10000);

select sqrt(number1) as root, log(number2) as log from decimals;