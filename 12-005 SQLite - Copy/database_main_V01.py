import sqlite3
import os

def print_table(cursor):
    cursor.execute('SELECT * FROM python_programming')
    rows = cursor.fetchall()
    print("Current table:")
    for row in rows:
        print(row)
    print()  # Add a new line for spacing

# Delete the existing database file if it exists
if os.path.exists('python_programming.db'):
    os.remove('python_programming.db')

# Connecting to the database and creating one if it doesn't exist
conn = sqlite3.connect('python_programming.db')
cursor = conn.cursor()

# 1st step: creating a table called python_programming
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
''')

print_table(cursor)

# 2nd step: inserting new rows into the python_programming table
rows_to_insert = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99),
]
cursor.executemany('INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)', rows_to_insert)

print_table(cursor)

# 3rd step: selecting all records with a grade between 60 and 80
cursor.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')
selected_rows = cursor.fetchall()
print("Selected rows with grades between 60 and 80:")
for row in selected_rows:
    print(row)

# 4th step: changing Carl Davis's grade to 65
cursor.execute('UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"')
print('Table with Carl age updated')
print_table(cursor)

# 5th step: deleting Dennis Fredrickson's row
cursor.execute('DELETE FROM python_programming WHERE name = "Dennis Fredrickson"')
print('Table after deleting Dennis row')
print_table(cursor)

# 6th step: changing the grade of all students with an id greater than 55 to 80
cursor.execute('UPDATE python_programming SET grade = 80 WHERE id > 55')
print('Table after changing the grade of all students with an id greater than 55 to 80')
print_table(cursor)

# Committing changes and closing the connection
conn.commit()
conn.close()