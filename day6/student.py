import sqlite3

students = [
    ("Amina", 90),
    ("Rahul", 60),
    ("Sneha", 95),
    ("Arjun", 50),
    ("Fatima", 92)
]

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            marks INTEGER
        )
    """)

    for student in students:
        cursor.execute(
            "INSERT INTO students (name, marks) VALUES (?, ?)",
            student
        )

    conn.commit()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    print("Students Table:")
    for row in rows:
        print(row)
      