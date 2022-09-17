--1
SELECT DISTINCT country
FROM customers
ORDER BY country DESC;
-- by default ASC
--2
SELECT DISTINCT country, city
FROM customers
ORDER BY country, city DESC;
-- AGGREGATE functions:MAX-MIN-SUM-AVG-COUNT
--3
SELECT MAX(unitprice)
FROM order_details;
--4
SELECT MIN(unitprice)
FROM order_details;
--5
SELECT AVG(unitprice)
FROM order_details;
--6
SELECT SUM(unitprice)
FROM order_details;
--7
SELECT unitprice
FROM order_details
ORDER BY unitprice;