-- LEFT JOIN
SELECT companyname, orderid
FROM customers
         LEFT JOIN orders ON customers.customerid = orders.customerid;

-- RIGHT JOIN
SELECT companyname, orderid
FROM customers
         RIGHT JOIN orders ON customers.customerid = orders.customerid;

-- FULL JOIN
SELECT companyname, orderid
FROM customers
         FULL JOIN orders ON customers.customerid = orders.customerid;