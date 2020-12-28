drop table if exists city;
drop table if exists country;

create table city (
	id int,
	name varchar(17),
	countrycode varchar(3),
	district varchar(20),
	population int
);

create table country (
	code varchar(3),
	name varchar(44),
	continent varchar(13),
	region varchar(25),
	surfacearea int,
	indepyear varchar(5),
	population int,
	lifeexpectancy varchar(4),
	gnp int,
	gnpold varchar(9),
	localname varchar(44),
	governmentform varchar(44),
	headofstate varchar(32),
	capital varchar(4),
	code2 varchar(2)
);

select country.continent, floor(avg(city.population))
from country
inner join city
on city.countrycode = country.code
group by country.continent;