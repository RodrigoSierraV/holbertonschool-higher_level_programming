-- script that creates the table force_name on your MySQL server.
-- force_name description:id INT and name VARCHAR(256) cant be null
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, script not fail

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
	
