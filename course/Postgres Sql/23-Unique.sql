-- solve 1
CREATE TABLE test
(
    id   integer PRIMARY KEY,
    name text UNIQUE
);

-- solve 2
ALTER TABLE test
    ADD email varchar(300) UNIQUE;
INSERT INTO test(id, name, email)
values (10, 'hamide', 'hamidezandi@gamil.com');