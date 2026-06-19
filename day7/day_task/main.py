from fastapi import FastAPI

from routers import tasks
from database import create_table

app = FastAPI(
    title="Task Manager API",
    version="2.0.0"
)

create_table()

app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)


@app.get("/")
def home():
    return {
        "message":
        "Persistent Task API using SQLite"
    }