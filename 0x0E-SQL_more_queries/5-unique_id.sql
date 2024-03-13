-- Write a script that creates the table unique_id on your MySQL server.
-- unique_id description:
--      id INT default value 1 must be uniqe
--      name VARCHAR(256) can’t be null
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);