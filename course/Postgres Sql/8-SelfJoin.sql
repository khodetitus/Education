SELECT e1.birthdate, e2.birthdate
FROM employees e1,
     employees e2
WHERE e1.birthdate > e2.birthdate;