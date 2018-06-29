# STADION: Club	Location	Capacity	stadium_id
# TRAINER: Name	DOB	Club	trainer_id
# RUNNER: Name	DOB	Club	gender	trener_id
# COMPETITON: stadium_id	date	attendence	weather	competition_id
# RESULT: Name	DOB	Club	gender	result	discipline	date	competition_id	result_id
CREATE TABLE STADION (
	Club CHAR,
	Location CHAR, 
	Capacity INT,
	stadium_id INT,
	PRIMARY KEY (stadium_id)
	);
CREATE TABLE TRAINER (
	Name CHAR,
	DOB DATETIME,
	Club CHAR,
	trainer_id INT,
	PRIMARY KEY (trainer_id)
	);
CREATE TABLE RUNNER (
	Name CHAR,
	DOB DATETIME,
	Club CHAR,
	gender VARCHAR(1);
	trener_id INT,
	PRIMARY KEY (NAME, DOB, gender)
	);
CREATE TABLE COMPETITON (
	stadium_id INT,
	date DATETIME,
	attendence VARCHAR(1),
	weather CHAR(8),
	competition_id CHAR(8),
	PRIMARY KEY (stadium_id, date)
	);
CREATE TABLE RESULT (
	DOB DATETIME ,
	Club CHAR,
	gender VARCHAR(1),
	result FLOAT,
	discipline CHAR,
	date DATETIME,
	competition_id INT,
	result_id INT,
	PRIMARY KEY (DOB, Club, gender, result, discipline, date, competition_id, result_id)
	);