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

select distinct city
from station
where city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';

select distinct city
from station
where city like '[A, E, I, O, U]%[a, e, i, o, u]';

select distinct city
from station
where city not like '[A, E, I, O, U]%';

select distinct city
from station
where city not like '%[A, E, I, O, U]';

select distinct city
from station
where city not like '[A, E, I, O, U]%' or city not like '%[a, e, i, o, u]';

select distinct city
from station
where city not like '[A, E, I, O, U]%' and city not like '%[a, e, i, o, u]';

--Query for Sum of All Values in lat_n Rounded to a Scale of Two Decimal Places
--Query for Sum of All Values in long_w Rounded to a Scale of Two Decimal Places
select cast(round(sum(lat_n), 2) as decimal(18, 2)), cast(round(sum(long_w), 2) as decimal(18, 2))
from station;

--Query the Sum of Northern Latitudes from Station Having Values Greater Than 38.7880 and Less Than 137.2345
--Truncate Your Answer to 4 Decimal Places
select cast(sum(lat_n) as decimal(18, 4))
from station
where lat_n > 38.7880 and lat_n < 137.2345;

--Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. 
--Truncate your answer to 4 decimal places.
select cast(max(lat_n) as decimal(18, 4))
from station
where lat_n < 137.2345;

--Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. 
--Round your answer to 4 decimal places.
select top 1 cast(long_w as decimal(18, 4))
from station
where lat_n < 137.2345
order by lat_n desc;

--Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. 
--Round your answer to 4 decimal places.
select top 1 cast(lat_n as decimal(18, 4))
from station
where lat_n > 38.7780
order by lat_n asc;

--Query the Western Longitude (LONG_W) where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. 
--Round your answer to 4 decimal places.
select top 1 cast(long_w as decimal(18, 4))
from station
where lat_n > 38.7780
order by lat_n asc;

--Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.
select cast(abs(max(lat_n) - min(lat_n)) + abs(max(long_w) - min(long_w)) as decimal(18, 4))
from station;

--Query the Euclidean Distance between points P1 and P2 and format your answer to display 4 decimal digits.
select cast(sqrt(power(abs(max(lat_n) - min(lat_n)), 2) + power(abs(max(long_w) - min(long_w)), 2)) as decimal(18, 4))
from station;

--Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.
select cast(lat_n as decimal(18, 4))
from station
order by lat_n asc
offset 
	(select count(*)/2
	from station) rows
fetch next 1 row only;