--1
SELECT *
FROM employees;
--2
SELECT firstname, lastname
FROM employees;
--3
SELECT country
FROM customers;
--4
SELECT DISTINCT country
FROM customers;
--5
SELECT COUNT(*)
FROM customers;
--6
SELECT COUNT(DISTINCT country)
FROM customers;
--7
SELECT customerid, shippeddate - orderdate
FROM orders;