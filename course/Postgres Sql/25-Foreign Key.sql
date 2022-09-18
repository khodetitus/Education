CREATE TABLE groups
(
    groupid    integer PRIMARY KEY,
    customerid varchar(10),
    name       text UNIQUE,
    FOREIGN KEY (customerid) REFERENCES customers (customerid)
);