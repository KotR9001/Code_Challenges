drop table if exists triangles;

create table triangles (
	A int, B int, C int, type varchar
);

select *
from triangles;

select
case
	when (a + b > c) and (b + c > a) and (a + c > b) then
	case
		when (a = b) and (b = c) and (a = c)
		then 'Equilateral'
		when (a = b) or (b = c) or (a = c)
		then 'Isosceles'
		else 'Scalene'
	end
	else 'Not A Triangle'
end
from triangles;
	