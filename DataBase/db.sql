CREATE TABLE fatalsbycounty (
	county VARCHAR(30) PRIMARY KEY,
	fatals INT,
	peds INT,
	persons INT,
	totalvehicle INT
);

CREATE TABLE fatalsbyhour (
	hour INT,
	fatals INT,
	peds INT,
	persons INT,
	totalvehicles INT

);
CREATE TABLE fatalsbymonth (
	month INT PRIMARY KEY,
	fatals INT,
	peds INT,
	persons INT,
	totalvehicles INT
);
CREATE TABLE wakecountyfatals (
	index INT,
	county VARCHAR(30),
	year INT,
	fatals INT,
	latitude FLOAT,
	longitude FLOAT,
	 totalvehicles INT
);
 
CREATE TABLE wakecountyfatals (
	index INT,
	county VARCHAR(30) PRIMARY KEY,
	year INT,
	fatals INT,
	latitude FLOAT,
	longitude FLOAT,
	 totalvehicles INT
);
