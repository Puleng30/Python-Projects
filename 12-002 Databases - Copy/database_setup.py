import sqlite3

# Step 3: Create the database file School.db
conn = sqlite3.connect("School.db")
cursor = conn.cursor()

# Step 4: Execute the create_table.sql script to create the table
with open("create_table.sql", "r") as create_table_script:
    cursor.executescript(create_table_script.read())

conn.commit()
conn.close()
