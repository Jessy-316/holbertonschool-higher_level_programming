-- Write a script that creates the table unique_id on your MySQL server
-- description of table data: id INT with the default value 1, must be unique & name VARCHAR(256)
-- should not fail if exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
