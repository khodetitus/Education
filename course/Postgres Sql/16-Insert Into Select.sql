SELECT *
FROM testing;

-- 1 with using name column
INSERT INTO testing(country)
SELECT country
FROM customers
WHERE country = 'Mexico';

-- 2 without using name column
INSERT INTO testing
SELECT *
FROM customers
WHERE country = 'Mexico';