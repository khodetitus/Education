CREATE TABLE test
(
    id   integer,
    name text DEFAULT 'masoud'

);
INSERT INTO test(id, name)
values (10, 'kaveh');
INSERT INTO test(id)
values (12)