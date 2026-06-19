import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students WHERE marks > 70")

for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")

conn.close()