drop table if exists company;
drop table if exists lead_manager;
drop table if exists senior_manager;
drop table if exists manager;
drop table if exists employee;

create table if not exists company (
	company_code varchar primary key,
	founder varchar
);

create table if not exists lead_manager (
	lead_manager_code varchar primary key,
	company_code varchar
);

create table if not exists senior_manager (
	senior_manager_code varchar primary key,
	lead_manager_code varchar,
	company_code varchar
);

create table if not exists manager (
	manager_code varchar primary key,
	senior_manager_code varchar,
	lead_manager_code varchar,
	company_code varchar
);

create table if not exists employee (
	employee_code varchar primary key,
	manager_code varchar,
	senior_manager_code varchar,
	lead_manager_code varchar,
	company_code varchar
);

select *
from company;

select *
from lead_manager;

select *
from senior_manager;

select *
from manager;

select *
from employee;

--Join the Tables & Print Company Code, Founder Name, Total Number of Lead Managers, Total Number of Senior Managers, 
--Total Number of Managers, & Total Number of Employees
select distinct company.company_code, company.founder, count(distinct employee.lead_manager_code), count(distinct employee.senior_manager_code), 
    count(distinct employee.manager_code), count(distinct employee.employee_code)
from company
inner join employee
on company.company_code = employee.company_code
group by company.company_code, company.founder
order by company.company_code asc;

--Found Method to Sort Rows by One Column and Only Return One Row per Distinct Value--
select company.company_code, company.founder, count(a.lead_manager_code), count(b.senior_manager_code), 
    count(c.manager_code), count(d.employee_code)
from company
left join (
	select *, 
	row_number() over(partition by lead_manager.company_code order by lead_manager.company_code) rn
	from lead_manager
	) a
on company.company_code = a.company_code
and a.rn = 1
left join (select *,
			row_number() over(partition by senior_manager.company_code order by senior_manager.company_code) rn
			from senior_manager) b
on a.company_code = b.company_code
and b.rn = 1
left join (select *,
			row_number() over(partition by manager.company_code order by manager.company_code) rn
			from manager) c
on b.company_code = c.company_code
and c.rn = 1
left join (select *,
			row_number() over(partition by employee.company_code order by employee.company_code) rn
			from employee) d
on c.company_code = d.company_code
and d.rn = 1
group by company.company_code, company.founder, a.lead_manager_code, b.senior_manager_code, c.manager_code, 
    d.employee_code
order by company.company_code asc;

select company.company_code, company.founder, count(a.lead_manager_code), count(b.senior_manager_code), 
    count(c.manager_code), count(d.employee_code)
from company
cross apply (
	select company.company_code, company.founder, count(lead_manager.lead_manager_code)
	from lead_manager
	where company.company_code = lead_manager.company_code
	group by company.company_code, company.founder, lead_manager.lead_manager_code
	) a
cross apply (
	select count(senior_manager.senior_manager_code)
	from senior_manager
	where a.lead_manager_code = senior_manager.lead_manager_code
	group by senior_manager.senior_manager_code
	) b
cross apply (
	select count(manager.manager_code)
	from manager
	where b.senior_manager_code = manager.senior_manager_code
	group by manager.manager_code
	) c
cross apply (
	select count(employee.employee_code)
	from employee
	where c.manager_code = employee.manager_code
	group by employee.employee_code
	) d
order by company.company_code asc;