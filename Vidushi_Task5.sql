CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(50),
    region VARCHAR(50),
    sale_amount INT,
    sale_date DATE
);

INSERT INTO sales (employee_name, region, sale_amount, sale_date) VALUES
('Alice', 'North', 1200, '2024-01-10'),
('Bob', 'North', 1800, '2024-01-12'),
('Charlie', 'North', 1700, '2024-01-15'),
('Diana', 'South', 1600, '2024-01-11'),
('Eve', 'South', 2000, '2024-01-13'),
('Frank', 'South', 1500, '2024-01-17'),
('Grace', 'East', 2200, '2024-01-09'),
('Heidi', 'East', 1900, '2024-01-14'),
('Ivan', 'East', 2100, '2024-01-20');

--Q1
SELECT sale_id,employee_name,region,sale_amount,sale_date,
ROW_NUMBER() OVER (ORDER BY sale_amount DESC) AS row_num
FROM sales;

--Q2
SELECT sale_id,employee_name,region,sale_amount,sale_date,
RANK() OVER (PARTITION BY region ORDER BY sale_amount DESC) AS regional_rank
FROM sales;

--Q3
SELECT sale_id,employee_name,region,sale_amount,sale_date,
RANK() OVER (PARTITION BY region ORDER BY sale_amount DESC) AS regional_rank,
DENSE_RANK() OVER (PARTITION BY region ORDER BY sale_amount DESC) AS dense_regional_rank
FROM sales;

--Q4
SELECT sale_id,employee_name,region,sale_amount,sale_date,
LAG(sale_amount) OVER (PARTITION BY region ORDER BY sale_date) AS previous_sale_amount,
sale_amount - LAG(sale_amount) OVER (PARTITION BY region ORDER BY sale_date) AS sale_difference
FROM sales;

--Q5
SELECT sale_id,employee_name,region,sale_amount,sale_date,
SUM(sale_amount) OVER (PARTITION BY region ORDER BY sale_date) AS previous_sale_amount,
sale_amount - LAG(sale_amount) OVER (PARTITION BY region ORDER BY sale_date) AS sale_difference
FROM sales;

--Q6
SELECT sale_id,employee_name,region,sale_amount,sale_date,
MAX(sale_amount) OVER (PARTITION BY region ORDER BY sale_amount DESC) AS max_sale
FROM sales;

--Q7
SELECT sale_id,employee_name,region,sale_amount,sale_date,
FIRST_VALUE(sale_amount) OVER (PARTITION BY region ORDER BY sale_date) AS first_sale,
LAST_VALUE(sale_amount) OVER (PARTITION BY region ORDER BY sale_date 
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_sale
FROM sales;

--Q8
SELECT sale_id,employee_name,region,sale_amount,sale_date,
NTILE(3) OVER (ORDER BY sale_amount DESC) AS sale_tiers
FROM sales;