from fastapi import FastAPI
from routers import tasks

app = FastAPI(
    title="Task Manager API",
    description="Day 5 — Full CRUD with in-memory storage",
    version="1.0.0"
)

app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)

@app.get("/")
def home():
    return {"message": "Task API is running !"}