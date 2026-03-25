import sqlite3
from database import DB_NAME

def add_task(user_id, title, description=""):
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        "INSERT INTO tasks (user_id, title, description) VALUES (?, ?, ?)",
        (user_id, title, description)
    )
    conn.commit()
    conn.close()

def get_tasks(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute(
        "SELECT id, title, description, status FROM tasks WHERE user_id = ?",
        (user_id,)
    )
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id, title, description, status):
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        "UPDATE tasks SET title=?, description=?, status=? WHERE id=?",
        (title, description, status, task_id)
    )
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()