-- AS
-- 1
SELECT quantity * unitprice AS Total
FROM order_details;

-- 2
SELECT quantity * unitprice AS Total
FROM order_details
ORDER BY Total DESC;

-- LIMIT
-- 3
SELECT quantity * unitprice AS Total
FROM order_details
ORDER BY Total DESC
LIMIT 30;

-- null & IS
-- 4
SELECT companyname, region
FROM customers
WHERE region IS null;

-- NOT
-- 5
SELECT companyname, region
FROM customers
WHERE region IS NOT null
ORDER BY region DESC;