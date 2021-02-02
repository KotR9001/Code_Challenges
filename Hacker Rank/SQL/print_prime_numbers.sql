declare @num int
declare @num1 int
declare @non_prime_list varchar
declare @prime_list varchar
declare @non_prime_string varchar
declare @prime_string varchar

set @num = 2
set @num1 = 2
set @non_prime_string = ""
set @prime_string = ""

create table bool_list_list (
    bool_list varchar
);

create table non_prime_list (
    character1 varchar
);

create table prime_list (
    character2 varchar
);


while (@num < 10)
begin
    drop table if exists bool_list;
    create table bool_list (
        boolean varchar
    );
    while (@num1 < 10)
    begin
        while @num > @num1
		begin
			if @num % @num1 = 0
			begin
				insert into bool_list
				values ('True')
			end
			else
			begin
				insert into bool_list
				values ('False')
			end
		end
	set @num1 = @num1 + 1
	end
	select cast(@num as varchar)
	update prime_list
	set @prime_string = concat(@prime_string, @num, '&')
	where boolean != any(select * from bool_list where boolean = 'True')
	select cast(@num as integer)
set @num = @num + 1
end
print @prime_string;