SELECT productname, SUM(quantity * order_details.unitprice) AS Total
FROM order_details
         JOIN products ON order_details.productid = products.productid
GROUP BY productname
-- HAVING Total >20000    Not using with AS name
HAVING SUM(quantity * order_details.unitprice) > 2000
ORDER BY Total;
