drop table if exists documents;

create table if not exists documents (
	id integer,
	data text
);

select * from documents;

drop table if exists document_changelog;

create table if not exists document_changelog (
	id integer,
	document_id integer, 
	old_data text, 
	new_data text
);

select * from document_changelog;

INSERT INTO documents_changelog(document_id, old_data, new_data) VALUES (-1, NULL, NULL);