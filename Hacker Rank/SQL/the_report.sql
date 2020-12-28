drop table if exists students;
drop table if exists grades;

create table students (
	id int,
	name varchar,
	marks int
);

create table grades (
	grade int,
	min_mark int,
	max_mark int
);

drop view if exists student_grades;

update students
set name = null
select students.name, grades.grade, students.marks
from students
inner join grades
on students.marks between grades.min_mark and grades.max_mark
where marks < 8
order by 
	case when students.marks < 8 then
		grades.grade end desc,
	case when students.marks < 8 then
		students.marks end asc,
	case when students.marks >= 8 then
		grades.grade end desc, 
	case when students.marks >= 8 then
		students.name end asc;
		
select *
from student_grades;
		
update students
set students.name = null
from grades
on students.marks between grades.min_mark and grades.max_mark
where students.marks < 8
order by 
    case when students.marks < 8 then
        grades.grade end desc,
    case when students.marks < 8 then
        students.marks end asc,
    case when students.marks >= 8 then
        grades.grade end desc, 
    case when students.marks >= 8 then
        students.name end asc;