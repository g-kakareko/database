-- STADION: Club	Location	Capacity	stadium_id
-- TRAINER: Name	DOB	Club	trainer_id
-- RUNNER: Name	DOB	Club	gender	trener_id
-- COMPETITON: stadium_id	date	attendence	weather	competition_id
-- RESULT: Name	DOB	Club	gender	result	discipline	date	competition_id	result_id
CREATE TABLE STADION (
	Club CHAR(100),
	Location CHAR(100), 
	Capacity INT,
	stadium_id INT,
	PRIMARY KEY (Location)
	);
CREATE TABLE TRAINER (
	Name CHAR(100),
	DOB DATETIME,
	Club CHAR(100)
	PRIMARY KEY (Name, DOB)
	);
CREATE TABLE RUNNER (
	Name CHAR(100),
	DOB DATETIME,
	Club CHAR(100),
	gender VARCHAR(1),
	tr_Name CHAR(100)
	PRIMARY KEY (Name, DOB)
	);
CREATE TABLE COMPETITON (
	Location CHAR(100),
	date_comp DATETIME,
	attendence INT,
	weather CHAR(1),
	competition_id INT,
	PRIMARY KEY (Location, date_comp)
	);
-- Name,DOB,Club,gender,result,discipline,date,competition_id,result_id
CREATE TABLE RESULT (
	Name CHAR(100),
	DOB DATETIME ,
	Club CHAR(100),
	gender VARCHAR(1),
	result FLOAT,
	discipline CHAR(100),
	date_comp DATETIME,
	Location CHAR(100),
	result_id INT,
	PRIMARY KEY (Name, DOB, Club, gender, result, discipline, date_comp, Location, result_id)
	);
-- Initializing the Tables:
-- Stadium
LOAD DATA LOCAL INFILE '/home/grzegorz/Desktop/Database/Project/database/initial_db/stadion.csv' INTO 
TABLE STADION FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Club, Location, Capacity, stadium_id)
;
-- Trainer
LOAD DATA LOCAL INFILE '/home/grzegorz/Desktop/Database/Project/database/initial_db/trainer.csv' INTO 
TABLE TRAINER FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Name, @DOB, Club, trainer_id)
SET DOB = STR_TO_DATE(@DOB, '%m-%d-%y')
;
-- Runner
LOAD DATA LOCAL INFILE '/home/grzegorz/Desktop/Database/Project/database/initial_db/runner.csv' INTO 
TABLE RUNNER FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Name, @DOB, Club, gender,trener_id)
SET DOB = STR_TO_DATE(@DOB, '%m-%d-%y')
;
-- Competition
LOAD DATA LOCAL INFILE '/home/grzegorz/Desktop/Database/Project/database/initial_db/compet.csv' INTO 
TABLE COMPETITON FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(stadium_id, @date_comp, attendence, weather, competition_id)
-- SET date_comp = STR_TO_DATE(@date_comp, '%Y-%m-%d')
SET date_comp = STR_TO_DATE(@date_comp, '%m-%d-%y')
;
-- Result
LOAD DATA LOCAL INFILE '/home/grzegorz/Desktop/Database/Project/database/initial_db/result60.csv' INTO 
TABLE RESULT FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(Name, @DOB, Club, gender, result, discipline, @date_comp, competition_id, result_id) 
SET DOB = STR_TO_DATE(@DOB, '%m-%d-%y'), date_comp = STR_TO_DATE(@date_comp, '%m-%d-%y')
;