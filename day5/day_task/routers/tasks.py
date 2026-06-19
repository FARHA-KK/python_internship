from fastapi import APIRouter, HTTPException
from schemas import TaskCreate, TaskUpdate, TaskResponse

router:  APIRouter = APIRouter()
tasks:   dict      = {}
next_id: int       = 1

# ── GET all tasks ──────────────────────────────────
@router.get("/", response_model=list[TaskResponse])
def get_all_tasks():
    return list(tasks.values())

# ── GET one task ───────────────────────────────────
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# ── POST create task ───────────────────────────────
@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    global next_id
    new_task = {"id": next_id, **task.model_dump()}
    tasks[next_id] = new_task
    next_id += 1
    return new_task

# ── PUT full update ────────────────────────────────
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = {"id": task_id, **task.model_dump()}
    tasks[task_id] = updated
    return updated

# ── PATCH partial update ───────────────────────────
@router.patch("/{task_id}", response_model=TaskResponse)
def partial_update(task_id: int, task: TaskUpdate):
    existing = tasks.get(task_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updates = {k: v for k, v in task.model_dump().items() if v is not None}
    existing.update(updates)
    tasks[task_id] = existing
    return existing

# ── DELETE task ────────────────────────────────────
@router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": f"Task {task_id} deleted successfully"}

# ── BONUS — PATCH mark complete ────────────────────
@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task["completed"] = True
    tasks[task_id]    = task
    return task