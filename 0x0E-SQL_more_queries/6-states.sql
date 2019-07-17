-- script that creates the database hbtn_0d_usa and the table states
-- states description: id INT unique, auto generated, cant be null and is a primary key and name VARCHAR(256) cant be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

