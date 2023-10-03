import sqlite3
import os

def create_table_if_not_exists():
    if not os.path.exists("School.db"):
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        with open("create_table.sql", "r") as create_table_script:
            cursor.executescript(create_table_script.read())
        conn.commit()
        conn.close()

def execute_script_file(script_file):
    with open(script_file, "r") as script:
        query = script.read()
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.executescript(query)
        conn.commit()
        conn.close()

def execute_query_file(query_file):
    with open(query_file, "r") as query_script:
        query = query_script.read()
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

if __name__ == "__main__":
    try:
        #creating the table if it doesn't exist
        create_table_if_not_exists()

        #creating the views using view_table.sql
        execute_script_file("view_table.sql")

        #executing failed.sql
        failed_result = execute_query_file("failed.sql")
        print("Failed Students:")
        for row in failed_result:
            print(row)

        #executing distinction.sql
        distinction_result = execute_query_file("distinction.sql")
        print("\nDistinction Students:")
        for row in distinction_result:
            print(row)

        #executing near_distinction.sql
        near_distinction_result = execute_query_file("near_distinction.sql")
        print("\nNear Distinction Students:")
        for row in near_distinction_result:
            print(row)

        #executing javascript_junkies.sql
        javascript_junkies_result = execute_query_file("javascript_junkies.sql")
        print("\nJavaScript Junkies (Web Dev Students):")
        for row in javascript_junkies_result:
            print(row)

    except sqlite3.Error as e:
        print("Error executing SQL query:", e)
