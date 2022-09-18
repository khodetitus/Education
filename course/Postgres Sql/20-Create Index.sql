-- Create index
CREATE UNIQUE INDEX email_users
    ON users (email);

-- Delete index
DROP INDEX email_users;