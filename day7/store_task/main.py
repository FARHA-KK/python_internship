from fastapi import FastAPI
from schemas import TaskCreate
from database import init_db, create_task

app = FastAPI()

init_db()

@app.post("/tasks")
def add_task(task: TaskCreate):
    return create_task(
        task.title,
        task.completed
    )