DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
student_id CHAR(13) PRIMARY KEY,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email varchar(30) NOT NULL,
stu_subject TEXT CHECK(stu_subject in ('Data Science', 'Software Engineering', 'Web Dev', 'Databases')) NOT NULL,
mark INTEGER NOT NULL);

INSERT INTO Student 
VALUES
('JV00100200304', 'Johnny', 'Valker', 'jv@email.com', 'Data Science', 64),
('JS00100200305', 'Jack', 'Sparrow', 'js@blackpearl.com', 'Web Dev', 52),
('LM00100200306', 'Luffy', 'Monkey', 'pking@linegrand.com', 'Web Dev', 43),
('PA00100200307', 'Paul', 'Atreides', 'paul@melange.com', 'Data Science', 78),
('LA00100200308', 'Leto', 'Atreides', 'leto@melange.com', 'Data Science', 92),
('AT00100200309', 'Alan', 'Turing', 'whereis@myemail.com', 'Software Engineering', 72),
('AL00100200310', 'Ada', 'Lovelace', 'motherof@computing.com', 'Software Engineering', 86),
('PP00100200311', 'Peter', 'Parker', 'pp@marvel.com', 'Web Dev', 83),
('AS00100200312', 'Anthony', 'Stark', 'ironman@marvel.com', 'Software Engineering', 95),
('KK00100200313', 'Kamala', 'Khan', 'ms@marvel.com', 'Data Science', 67),
('CD00100200314', 'Carol', 'Danvers', 'captain@marvel.com', 'Web Dev', 72),
('DV00100200315', 'Darth', 'Vader', 'dv@deathstar.com', 'Software Engineering', 62),
('AS00100200316', 'Anakin', 'Skywalker', 'ihatesand@deathstar.com', 'Software Engineering', 62),
('LS00100200317', 'Leia', 'Skywalker', 'leader@rebels.com', 'Data Science', 89),
('OK00100200318', 'Obi-Wan', 'Kenobi', 'hellothere@jedicouncil.com', 'Data Science', 70),
('GG00100200319', 'Gandalf', 'Grey', 'youshall@notpass.com', 'Web Dev', 27),
('JB00100200320', 'Johnny', 'Bravo', 'jb@cn.com', 'Databases', 69),
('PB00100200321', 'Pinky', 'Brain', 'pinky@brain.com', 'Data Science', 100),
('JS00100200322', 'John', 'Smith', 'doctor@who.com', 'Databases', 79),
('JS00100200323', 'Jane', 'Smith', 'professor@who.com', 'Databases', 92),
('EP00100200324', 'Elvis', 'Presley', 'elvis@elvis.com', 'Software Engineering', 56),
('FM00100200325', 'Frederick', 'Mercury', 'rhapsody@queen.com', 'Web Dev', 87),
('BC00100200326', 'Benedict', 'Cumberbatch', 'benny@strange.com', 'Databases', 65),
('WT00100200327', 'Wimbledon', 'Tennismatch', 'wimbeldon@strange.com', 'Databases', 68)