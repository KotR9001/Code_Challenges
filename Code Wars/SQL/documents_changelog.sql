drop table if exists documents;

create table if not exists documents (
	id integer,
	data text
);

select * from documents;

drop table if exists documents_changelog;

create table if not exists documents_changelog (
	id integer,
	document_id integer, 
	old_data text, 
	new_data text
);

select * from documents_changelog;

--Drop Existing Functions and Triggers
--Found Methods at https://www.postgresql.org/docs/9.1/sql-droptrigger.html &
--https://www.postgresql.org/docs/10/sql-dropfunction.html
drop function if exists insert_copy();
drop trigger if exists insert1 on documents_changelog;
drop function if exists update_copy();
drop trigger if exists update1 on documents_changelog;
drop function if exists delete_copy();
drop trigger if exists delete1 on documents_changelog;

--Insert Data
insert into documents
values (1, 'hello'), (2, 'world');

--Update Data
update documents set data='hi'
where data='hello';

--Delete Data
delete from documents
where data='hi';

--Create Function to Copy Inserted Data into New Table
--Found Method to Create Function at https://www.postgresql.org/docs/9.5/sql-createfunction.html
--and https://stackoverflow.com/questions/45504492/postgresql-trigger-to-update-a-column-in-a-table-when-another-table-gets-inserte
create function insert_copy()
returns trigger
as
$$
begin
	insert into documents_changelog (document_id, new_data)
	select new.id, new.data
	from documents;
	return documents_changelog.document_id, documents_changelog.new_data;
end;
$$language plpgsql;

--Create Trigger to Copy Inserted Data into New Table
--Found Method to Create Trigger at https://www.postgresql.org/docs/9.1/sql-createtrigger.html
create trigger insert1
after insert
on documents
for each row
execute procedure insert_copy();

--Create Function to Update Data
--Reviewed info at https://www.postgresql.org/docs/9.1/sql-update.html
create function update_copy()
returns trigger
as
$$
begin
insert into documents_changelog(documents.id, documents.old_data, documents.new_data)
values (documents.id, documents.data);
end;
$$language plpgsql;

--Create Trigger to Copy Updated Data into New Table
create trigger update1
after update
on documents_changelog
for each row
execute procedure update_copy();

--Create Function to Delete Data
--https://www.postgresql.org/docs/10/sql-delete.html
create function delete_copy()
returns trigger
as
$$
begin
insert into documents_changelog(document_id, old_data)
values (documents.id, documents.data);
end;
$$language plpgsql;

--Create Trigger to Copy Deleted Data into New Table
create trigger delete1
after delete
on documents_changelog
for each row
execute procedure delete_copy();

INSERT INTO documents_changelog(document_id, old_data, new_data) VALUES (-1, NULL, NULL);