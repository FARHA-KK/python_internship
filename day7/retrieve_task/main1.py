from fastapi import FastAPI
from schema import TaskCreate
from database1 import init_db, create_task, get_all_tasks

app = FastAPI()

init_db()

@app.post("/tasks")
def add_task(task: TaskCreate):
    return create_task(
        task.title,
        task.completed
    )

@app.get("/tasks")
def read_tasks():
    return get_all_tasks()