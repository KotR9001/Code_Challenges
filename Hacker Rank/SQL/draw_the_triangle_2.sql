declare @row_num int
set @row_num = 1
while (@row_num <= 20)
begin
    print replicate("* ", @row_num)
    set @row_num = @row_num + 1
end;