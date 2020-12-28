drop table if exists occupations;

create table occupations (
	Name varchar,
	Occupation varchar
);

select *
from occupations;

--Method to Use Union with Order By Found at https://stackoverflow.com/questions/13454815/using-different-order-by-with-union
select *
from(select concat(Name, '(', left(Occupation, 1), ')') as ordinal
from occupations
order by Name asc) as T1
union all
select *
from(select concat('There are a total of ', count(Occupation), ' ', lower(Occupation), 's.') as ordinal
from occupations
group by Occupation
order by count(Occupation) asc, Occupation desc) as T2
order by ordinal;