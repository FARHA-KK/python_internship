import sqlite3


conn = sqlite3.connect(
    "tasks.db",
    check_same_thread=False
)

cursor = conn.cursor()


# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    hashed_password TEXT
)
""")


# Tasks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    owner_email TEXT
)
""")


conn.commit()