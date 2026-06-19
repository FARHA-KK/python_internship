from fastapi import APIRouter, Depends, HTTPException

from database import cursor, conn

from schemas import TaskCreate

from auth import get_current_user



router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)



# Create task

@router.post("/")
def create_task(
    task: TaskCreate,
    user=Depends(get_current_user)
):

    cursor.execute(
        """
        INSERT INTO tasks
        (title,description,owner_email)
        VALUES(?,?,?)
        """,
        (
            task.title,
            task.description,
            user
        )
    )


    conn.commit()


    return {
        "message":"Task created"
    }




# Get only own tasks

@router.get("/")
def get_tasks(
    user=Depends(get_current_user)
):

    cursor.execute(
        """
        SELECT id,title,description
        FROM tasks
        WHERE owner_email=?
        """,
        (user,)
    )


    tasks = cursor.fetchall()


    return {
        "user":user,
        "tasks":tasks
    }





# Delete task

@router.delete("/{task_id}")
def delete_task(
    task_id:int,
    user=Depends(get_current_user)
):

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id=? AND owner_email=?
        """,
        (
            task_id,
            user
        )
    )


    conn.commit()


    return {
        "message":"deleted"
    }