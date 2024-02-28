-- File: mysql_learning_queries.sql

-- Create Schema
CREATE SCHEMA mysql_learning;
use  mysql_learning;

-- Create Table
CREATE TABLE mysql_learning (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT
);


-- Insert Data
INSERT INTO mysql_learning (username, email, age) 
VALUES ('john_doe', 'john@example.com', 30),
       ('jane_doe', 'jane@example.com', 25),
       ('alice', 'alice@example.com', 35);

-- Select All Users
SELECT * FROM mysql_learning;

SET SQL_SAFE_UPDATES = 0;

-- Select users with age greater than 25
SELECT * FROM mysql_learning WHERE age > 25;

-- Update Jane's age
UPDATE mysql_learning SET age = 10 WHERE username = 'jane_doe';

-- Delete user with username 'alice'
DELETE FROM mysql_learning WHERE username = 'alice';
