CREATE TABLE test
(
    name text,
--     age integer CONSTRAINT ch_age CHECk (age > 10) -->for single condition
    age  integer,
    CONSTRAINT ch_age CHECK (age > 10 AND LENGTH(name) > 4)
-- for multiple conditions

);
INSERT INTO test(name, age)
values ('masoud', 15);

-- Delete Constraint
ALTER TABLE test
    DROP CONSTRAINT ch_age;