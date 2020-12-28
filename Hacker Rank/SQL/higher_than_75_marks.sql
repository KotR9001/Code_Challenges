drop table if exists students;

create table students (
	id int,
	name varchar,
	marks int
);

select name 
from students
where marks > 75
order by right(name, 3), id asc;