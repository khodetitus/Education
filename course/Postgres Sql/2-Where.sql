-- 1
SELECT *
FROM customers
WHERE country = 'Germany';
--2
SELECT *
FROM order_details
WHERE quantity > 10;
--3
SELECT *
FROM order_details
WHERE quantity < 10;
--4
SELECT *
FROM orders
WHERE orderdate > '1996-7-8';
--5
SELECT *
FROM customers
WHERE country = 'Germany'
  AND city = 'Berlin';
--6
SELECT *
FROM customers
WHERE country = 'Germany'
   OR city = 'Paris';
--7
SELECT *
FROM customers
WHERE NOT country = 'Germany';
--8
SELECT *
FROM customers
WHERE NOT country = 'Mexico'
  AND (city = 'Berlin' OR city = 'Paris');
--9
SELECT *
FROM order_details
WHERE unitprice BETWEEN 10 AND 43;
--10
SELECT *
FROM customers
WHERE country IN ('Mexico', 'Germany', 'Spain')