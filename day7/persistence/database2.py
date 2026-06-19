import sqlite3

DB_NAME = "persistence.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

def create_task(title, completed):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(title, completed) VALUES (?, ?)",
        (title, completed)
    )

    conn.commit()
    task_id = cursor.lastrowid

    conn.close()

    return {
        "id": task_id,
        "title": title,
        "completed": completed
    }

def get_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]