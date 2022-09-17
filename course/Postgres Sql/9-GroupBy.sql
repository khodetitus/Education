-- 1
SELECT country,
       COUNT(*)
FROM customers
GROUP BY country;

-- 2
SELECT companyname, COUNT(freight), SUM(freight), ROUND(AVG(freight))
FROM customers
         JOIN orders ON customers.customerid = orders.customerid
GROUP BY companyname
ORDER BY companyname;
-- 3
SELECT productname, SUM(quantity * order_details.unitprice) AS Total
FROM order_details
         JOIN products ON order_details.productid = products.productid
         JOIN orders ON order_details.orderid = orders.orderid
WHERE orderdate BETWEEN '1997-01-01' AND '1997-12-31'
GROUP BY productname
ORDER BY Total;
