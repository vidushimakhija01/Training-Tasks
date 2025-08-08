create table projects (
project_id serial primary key,
project_name varchar(50),
start_date date default current_date
);
insert into projects(project_name) values ('Python');
insert into projects(project_name) values ('Javascript');
alter table projects add end_date date;
alter table projects drop end_date;
alter table projects rename to initiatives;
select * from initiatives;
truncate table initiatives;
select * from initiatives;
comment on table initiatives is 'Contains project details';
insert into initiatives(project_name,start_date) values ('Python', '2025-05-27');
insert into initiatives(project_name,start_date) values ('Javascript','2023-07-09');
select * from initiatives;
create table active_projects as select project_id, project_name from initiatives
where start_date >= current_date - interval '1 year';
select * from active_projects;