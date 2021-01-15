drop table if exists occupations;

create table occupations (
	name varchar,
	occupation varchar
);

select *
from occupations;

--Enable Crosstab--
create extension tablefunc;

--Create Pivot Table--
--Found Method at https://learnsql.com/blog/creating-pivot-tables-in-postgresql-using-the-crosstab-function/--
--and https://docs.microsoft.com/en-us/sql/t-sql/queries/from-using-pivot-and-unpivot?view=sql-server-ver15--
--and https://stackoverflow.com/questions/39505190/need-to-pivot-string-values-in-sql-server--
--PostgreSQL Method--
select *
from crosstab(
	'select *
	from occupations'
) as final_result(name varchar);

select Doctor, Professor, Singer, Actor
from (
    select *,
	--Found Method to Assign Values to Rows at https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-row_number-function/--
    row_number() over(partition by occupation order by name) as rn
    from occupations
) as source_table
pivot
(
max(name)
for occupation
    in (Doctor, Professor, Singer, Actor)
)
as pivot_table;