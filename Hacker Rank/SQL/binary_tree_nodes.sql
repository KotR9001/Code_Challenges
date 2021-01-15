drop table if exists bst;

create table bst (
	N int,
	P int
);

select *
from bst;

--Check if Value Exists in One or Both Columns--
--Hint Found at https://stackoverflow.com/questions/21800481/check-if-column-value-exists-in-another-column-in-sql--
select N,
	case
		when P is NULL then 'Root'
		else
			case
				when N in (select P from bst) then 'Inner'
				else 'Leaf'
			end
	end 
from bst
order by N;