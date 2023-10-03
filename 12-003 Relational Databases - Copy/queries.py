import sqlite3

#this function executes the query and fetchs results
def execute_query(query):
    connection = sqlite3.connect("School.db")
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

# 1st query: lists the names and surnames of all students doing the "DS03" course.
query1 = """
SELECT s.first_name, s.last_name
FROM Student AS s
INNER JOIN Course AS c ON s.stu_subject_code = c.course_code
WHERE c.course_code = 'DS03';
"""

# 2nd query: lists the email addresses of all students who are doing a level 3 course.
query2 = """
SELECT s.email
FROM Student AS s
INNER JOIN Course AS c ON s.stu_subject_code = c.course_code
WHERE c.course_level = 3;
"""

# 3rd query: lists the first names of all students that achieve a mark of 70 or above,
# along with the course name that they got a mark of 70 or above in.
query3 = """
SELECT s.first_name, c.course_name
FROM Student AS s
LEFT OUTER JOIN Course AS c ON s.stu_subject_code = c.course_code
WHERE s.mark >= 70;
"""

# 4th query: lists the marks of all students who have been taught by Julia Python.
query4 = """
SELECT s.first_name, s.last_name, s.mark
FROM Student AS s
LEFT OUTER JOIN Course AS c ON s.stu_subject_code = c.course_code
WHERE c.teacher_name = 'Julia Python';
"""

#executing each query and fetching the results
results_query1 = execute_query(query1)
results_query2 = execute_query(query2)
results_query3 = execute_query(query3)
results_query4 = execute_query(query4)

#displaying the results
print("Query 1: Names and Surnames of students doing 'DS03' course:")
for first_name, last_name in results_query1:
    print(f"{first_name} {last_name}")

print("\nQuery 2: Email addresses of students doing level 3 courses:")
for email_address in results_query2:
    print(email_address[0])

print("\nQuery 3: First names of students with a mark of 70 or above and their courses:")
for first_name, course_name in results_query3:
    print(f"{first_name} - {course_name}")

print("\nQuery 4: Marks of students taught by Julia Python:")
for first_name, last_name, mark in results_query4:
    print(f"{first_name} {last_name} - Mark: {mark}")
