drop table if exists city;

create table city (
	id int,
	name varchar(17),
	countrycode varchar(3),
	district varchar(20),
	population int
);

select *
from city
where population > 100000 and countrycode = 'USA';

select name
from city
where population > 120000 and countrycode = 'USA';