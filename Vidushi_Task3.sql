--TASK AGGREGATE FUNCTIONS
CREATE TABLE COURSE (
    COURSE_ID SERIAL PRIMARY KEY,
    COURSE_NAME VARCHAR(100) NOT NULL,
    START_DATE DATE
);
CREATE TABLE STUDENT (
    STUDENT_ID SERIAL PRIMARY KEY,
    STUDENT_NAME VARCHAR(100) NOT NULL,
    COURSE_ID INT REFERENCES COURSE(COURSE_ID),
    GRADE NUMERIC(5, 2),
    ENROLLMENT_DATE DATE
);

--#1
select c.course_name, count(s.student_id) from course c join student s
on c.course_id = s.course_id group by c.course_name;

--#2
select sum(grade) from student group by course_id;

--#3
select avg(grade) from student group by course_id;

--#4
select min(enrollment_date) from student group by course_id;

--#5
select max(grade) from student group by course_id;

--#6
select min(enrollment_date) from student group by course_id;

--#7
select max(enrollment_date) from student group by course_id;

--#8
select c.course_name from course c join student s on c.course_id = s.course_id
group by c.course_id having count(s.student_id) > 10;

--#9
select c.course_name, count(s.student_id) from course c join student s on c.course_id = s.course_id
group by c.course_id;

--#10
select c.course_name, sum(s.grade) from course c join student s on c.course_id = s.course_id
group by c.course_id;

--#11
select c.course_name, avg(s.grade) from course c join student s on c.course_id = s.course_id
group by c.course_id;

--#12
select c.course_name, round(avg(s.grade),2) from course c join student s on c.course_id = s.course_id
group by c.course_id;


--TASK SINGLE ROW FUNCTIONS
--#1
select concat(
    '(+',
    substring(contact_no, 1,2),
    ') ',
    substring(contact_no, 3, 5),
    '-',
    substring(contact_no, 8, 5))
    as formatted_contact from table contacts;

--#2
select concat(
    left(first_name, 1),
    last_name,
    right(employee_id, 2)
)as custom_id from employees;

--#3
replace(replace(replace(description, '*', ' '), '#', ' '), '@', ' ');

--#4
select email from users where email like '%@gmail.com' or email like '%@yahoo.com';

--#5
select concat(upper(substring(product_name, 1,1)),
lower(substring(product_name, 2,))) from products;