-- % sign
-- 1
SELECT *
FROM customers
WHERE companyname LIKE 'A%';

-- 2
SELECT *
FROM customers
WHERE companyname LIKE 'A%e';
-- 3
SELECT *
FROM customers
WHERE companyname LIKE 'A%e%';

-- _sign
--  1
SELECT *
FROM customers
WHERE companyname LIKE 'A_f%';