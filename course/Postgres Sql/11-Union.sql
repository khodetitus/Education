-- with using UNION
-- 1

SELECT companyname
FROM customers
UNION
SELECT companyname
FROM suppliers;

-- With using UNION ALL
-- 2
SELECT city
FROM customers
UNION ALL
SELECT city
FROM suppliers;