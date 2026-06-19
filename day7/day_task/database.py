import sqlite3

DB_NAME = "tasks.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def create_task(title, description, priority, completed):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO tasks(title, description, priority, completed)
        VALUES (?, ?, ?, ?)
        """,
        (title, description, priority, completed)
    )

    conn.commit()

    task_id = cur.lastrowid

    conn.close()

    return get_task(task_id)


def get_all_tasks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_task(task_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cur.fetchone()

    conn.close()

    return dict(row) if row else None


def update_task(task_id, title, description, priority, completed):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE tasks
        SET title=?, description=?, priority=?, completed=?
        WHERE id=?
        """,
        (title, description, priority, completed, task_id)
    )

    conn.commit()
    conn.close()

    return get_task(task_id)


def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()

    deleted = cur.rowcount

    conn.close()

    return deleted


def get_tasks_by_status(status):
    conn = get_connection()
    cur = conn.cursor()

    completed = 1 if status == "completed" else 0

    cur.execute(
        "SELECT * FROM tasks WHERE completed=?",
        (completed,)
    )

    rows = cur.fetchall()

    conn.close()

    return [dict(row) for row in rows]