--JOINS & SUBQUERIES
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT REFERENCES departments(dept_id)
);

--Departments
INSERT INTO departments (dept_id, dept_name, location) VALUES
(1, 'HR', 'Delhi'),
(2, 'IT', 'Mumbai'),
(3, 'Finance', 'Delhi'),
(4, 'Legal', 'Chennai');  -- This one has no employees

-- Employees
INSERT INTO employees (emp_id, emp_name, salary, dept_id) VALUES
(101, 'Ravi', 50000, 1),
(102, 'Sneha', 60000, 2),
(103, 'Amit', 45000, 2),
(104, 'Zoya', 70000, 3),
(105, 'Vikram', 30000, 1),
(106, 'Tina', 80000, NULL); -- Employee with no department

--#1
select e.emp_name, d.dept_name from
employees e left join departments d
on e.dept_id = d.dept_id;

--#2
select d.dept_name, e.emp_name from
employees e right join departments d
on e.dept_id = d.dept_id;

--#4
select e.emp_name, d.dept_name from employees e cross join departments d;

--TASK SUBQUERIES
--#1
select emp_name, salary from employees
where salary > (select avg(salary) from employees);

--#2
with dept_avg as (
    select dept_id, avg(salary) as avg_salary
    from employees
    group by dept_id
)
select d.dept_name, a.avg_salary
from dept_avg a
join departments d on a.dept_id = d.dept_id
where a.avg_salary > 50000;

--#3
with dept_avg as (
    select dept_id, avg(salary) as avg_salary
    from employees
    group by dept_id
)
select e.emp_name,d.dept_name, a.avg_salary
from dept_avg a
join departments d on a.dept_id = d.dept_id
join employees e on d.dept_id = e.dept_id;

--#4
select emp_name from employees where dept_id in
(select dept_id from departments where location = 'Delhi');