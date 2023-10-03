SELECT s.first_name, s.last_name
FROM Student AS s
INNER JOIN Course AS c ON s.course_code = c.course_code
WHERE c.course_code = 'DS03';
