SELECT s.first_name, s.last_name, s.mark
FROM Student AS s
LEFT OUTER JOIN Course AS c ON s.course_code = c.course_code
WHERE c.teacher_name = 'Julia Python';
