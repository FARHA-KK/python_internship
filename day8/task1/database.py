import sqlite3


conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    hashed_password TEXT
)
""")

conn.commit()