import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

name = input("Enter student name to delete: ")

cursor.execute("DELETE FROM students WHERE name = ?", (name,))
conn.commit()

print("Student deleted successfully.\n")

cursor.execute("SELECT * FROM students")

print("Remaining Students:")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")

conn.close()