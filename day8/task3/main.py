from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from database import conn, cursor
from models import UserRegister, UserLogin, TaskCreate

from auth import (
    hash_password,
    verify_password,
    create_token,
    get_current_user
)


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)



# Register

@app.post("/auth/register")
def register(user: UserRegister):

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )

    if cursor.fetchone():

        raise HTTPException(
            400,
            "Email already exists"
        )


    hashed = hash_password(
        user.password
    )


    cursor.execute(
        """
        INSERT INTO users(email, hashed_password)
        VALUES(?,?)
        """,
        (
            user.email,
            hashed
        )
    )


    conn.commit()


    return {
        "message": "User registered"
    }



# Login

@app.post("/auth/login")
def login(user: UserLogin):

    cursor.execute(
        """
        SELECT email, hashed_password
        FROM users
        WHERE email=?
        """,
        (user.email,)
    )


    data = cursor.fetchone()


    if data is None:

        raise HTTPException(
            401,
            "Invalid credentials"
        )


    email, hashed = data


    if not verify_password(
        user.password,
        hashed
    ):

        raise HTTPException(
            401,
            "Invalid credentials"
        )


    token = create_token(email)


    return {
        "token": token
    }




# 🔒 PROTECTED ROUTE

@app.get("/tasks")
def get_tasks(
    current_user: str = Depends(get_current_user)
):

    cursor.execute(
        """
        SELECT id,title
        FROM tasks
        WHERE owner_email=?
        """,
        (current_user,)
    )


    tasks = cursor.fetchall()


    return {
        "user": current_user,
        "tasks": tasks
    }



# Create task (also protected)

@app.post("/tasks")
def create_task(
    task: TaskCreate,
    current_user: str = Depends(get_current_user)
):

    cursor.execute(
        """
        INSERT INTO tasks(title, owner_email)
        VALUES(?,?)
        """,
        (
            task.title,
            current_user
        )
    )


    conn.commit()


    return {
        "message": "Task created"
    }