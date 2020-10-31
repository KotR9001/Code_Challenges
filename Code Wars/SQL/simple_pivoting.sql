drop table if exists products;
drop table if exists details;

create table if not exists products (
	id integer primary key,
	name varchar
);

create table if not exists details (
	id integer primary key,
	product_id integer,
	detail varchar,
	constraint pid foreign key (product_id) references products(id)
);

select *
from products;

select *
from details;

drop view if exists prod_det;
drop view if exists good;
drop view if exists ok;
drop view if exists bad;

create view prod_det as (
	select products.id as product_id, products.name as name, details.id as detail_id, detail
	from products
	join details
	on products.id = details.product_id
);

create view good as (
	select distinct name, count(detail) filter (where detail = 'good') as good
	from prod_det
	group by name, detail
	having count(detail) filter (where detail = 'good') != 0
	order by name
);

create view ok as (
	select distinct name, count(detail) filter (where detail = 'ok') as ok
	from prod_det
	group by name, detail
	having count(detail) filter (where detail = 'ok') != 0
	order by name
);

create view bad as (
	select distinct name, count(detail) filter (where detail = 'bad') as bad
	from prod_det
	group by name, detail
	having count(detail) filter (where detail = 'bad') != 0
	order by name
);

select good.name, good, ok, bad
from good
join ok
on good.name = ok.name
join bad
on ok.name = bad.name;