SELECT s.email_address
FROM Student AS s
INNER JOIN Course AS c ON s.course_code = c.course_code
WHERE c.course_level = 3;
