from fastapi import FastAPI
from pydantic import BaseModel
from database2 import init_db, create_task, get_all_tasks

app = FastAPI()

init_db()

class Task(BaseModel):
    title: str
    completed: bool = False

@app.post("/tasks")
def add_task(task: Task):
    return create_task(
        task.title,
        task.completed
    )

@app.get("/tasks")
def read_tasks():
    return get_all_tasks()