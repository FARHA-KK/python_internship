from fastapi import FastAPI,HTTPException
app=FastAPI()
tasks = {
     1: {"id": 1, "title": "Study Python"},
    2: {"id": 2, "title": "Learn FastAPI"}
}
@app.post("/tasks")
def create_task(task: dict):
    task_id = task["id"]
    tasks[task_id] = task
    return {"message": "Task added successfully", "task": task}
@app.get("/tasks")
def get_tasks():
    return tasks
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks.pop(task_id)
    return {"message": "Task deleted successfully", "task": deleted_task}