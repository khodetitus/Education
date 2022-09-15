-- JOIN & ON
-- 1
SELECT companyname, orderdate, shipcountry
FROM customers
         JOIN orders ON customers.customerid = orders.customerid;

-- 2
SELECT companyname, orderdate, shipcountry, firstname
FROM customers
         JOIN orders On customers.customerid = orders.customerid
         JOIN employees ON orders.employeeid = employees.employeeid