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