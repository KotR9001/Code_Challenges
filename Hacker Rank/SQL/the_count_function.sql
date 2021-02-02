drop table if exists city;

create table city (
	id integer,
	name varchar(17),
	countrycode varchar(3),
	district varchar(20),
	population integer
);

--Query the Amount of Cities Having a Population Greater Than 100,000
select count(name)
from city
where population > 100000;

--Query the Total Population of Cities Where District is California
select sum(population)
from city
where district = 'California';

--Query the Average Population of Cities Where District is California
select avg(population)
from city
where district = 'California';

--Query the Average Population of All Cities Rounded Down
select floor(avg(population))
from city;

--Query the Sum of Populations for All Japanese Cities
select sum(population)
from city
where countrycode = 'JPN';

--Query the Difference Between the Maximum and Minimum Populations
select max(population) - min(population) as difference
from city;