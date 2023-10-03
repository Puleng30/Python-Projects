SELECT s.first_name, c.course_name
FROM Student AS s
LEFT OUTER JOIN Course AS c ON s.course_code = c.course_code
WHERE s.mark >= 70;
