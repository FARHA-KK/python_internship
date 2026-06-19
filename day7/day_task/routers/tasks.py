from fastapi import APIRouter, HTTPException, Query

from schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

from database import (
    create_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task,
    get_tasks_by_status
)

router = APIRouter()


@router.get("/", response_model=list[TaskResponse])
def get_tasks(status: str | None = Query(default=None)):

    if status:
        return get_tasks_by_status(status)

    return get_all_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_single_task(task_id: int):

    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=201
)
def add_task(task: TaskCreate):

    return create_task(
        task.title,
        task.description,
        task.priority,
        task.completed
    )


@router.put("/{task_id}",
            response_model=TaskResponse)
def replace_task(task_id: int, task: TaskCreate):

    existing = get_task(task_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return update_task(
        task_id,
        task.title,
        task.description,
        task.priority,
        task.completed
    )


@router.patch("/{task_id}",
              response_model=TaskResponse)
def patch_task(task_id: int, task: TaskUpdate):

    existing = get_task(task_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    updated = existing.copy()

    for key, value in task.model_dump().items():
        if value is not None:
            updated[key] = value

    return update_task(
        task_id,
        updated["title"],
        updated["description"],
        updated["priority"],
        updated["completed"]
    )


@router.delete("/{task_id}")
def remove_task(task_id: int):

    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message":
        f"Task {task_id} deleted successfully"
    }


@router.patch(
    "/{task_id}/complete",
    response_model=TaskResponse
)
def complete_task(task_id: int):

    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return update_task(
        task_id,
        task["title"],
        task["description"],
        task["priority"],
        True
    )