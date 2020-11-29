drop table if exists station;

create table station (
	id int,
	city varchar(21),
	state varchar(2),
	lat_n int,
	long_w int
);

select city, state
from station;

select distinct city
from station
where mod(id, 2) = 0;

select count(city) - count(distinct city)
from station;

(select city, length(city)
from station
group by city
order by length(city) asc, city asc
limit 1)
union
(select city, length(city)
from station
group by city
order by length(city) desc, city asc
limit 1);

select distinct city
from station
where city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%';