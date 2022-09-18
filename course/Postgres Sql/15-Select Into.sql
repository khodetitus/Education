SELECT *
FROM testing;
SELECT *
INTO testing
FROM customers
WHERE country IN ('Spain', 'Germany')