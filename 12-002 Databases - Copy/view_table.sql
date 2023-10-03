-- view_table.sql

-- View for failing students (marks <= 44)
CREATE VIEW failing_students AS
SELECT first_name, last_name, email
FROM Student
WHERE mark <= 44;

-- View for distinction students (marks >= 80)
CREATE VIEW distinction_students AS
SELECT first_name, last_name
FROM Student
WHERE mark >= 80;

-- View for near distinction students (marks between 70 and 79 inclusive)
CREATE VIEW near_distinction_students AS
SELECT email
FROM Student
WHERE mark BETWEEN 70 AND 79;

-- View for students doing Web Dev
CREATE VIEW web_dev_students AS
SELECT *
FROM Student
WHERE stu_subject = 'Web Dev';
