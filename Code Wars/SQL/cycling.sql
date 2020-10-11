drop table if exists cycling;

create table if not exists cycling (
	id integer,
	hours float
);

insert into cycling (id, hours)
values (1, 5), (2, 6.6), (3, 9.8);

select * from cycling;

select id, hours, FLOOR(0.5 * hours) as liters
from cycling;