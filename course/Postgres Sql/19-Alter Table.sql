-- Change the name Columns
ALTER TABLE users
    RENAME username To firstname;

-- Change the name tables
ALTER TABLE users
    RENAME TO all_users;

-- Add the column in tables
ALTER TABLE users
    ADD password varchar(300);

-- Delete the column in tables
ALTER TABLE users
    DROP COLUMN password;

-- Change the data type in columns
ALTER TABLE users
    ALTER COLUMN email SET DATA TYPE varchar(500)