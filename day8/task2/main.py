from fastapi import FastAPI, HTTPException, Depends

from database import conn, cursor
from models import UserRegister, UserLogin
from auth import (
    hash_password,
    verify_password,
    create_token,
    get_current_user
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Authentication API"
    }


# ---------------- REGISTER ----------------

@app.post("/auth/register")
def register(user: UserRegister):

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(
        user.password
    )

    cursor.execute(
        """
        INSERT INTO users(email, hashed_password)
        VALUES (?, ?)
        """,
        (
            user.email,
            hashed_password
        )
    )

    conn.commit()

    return {
        "message": "User registered successfully"
    }


# ---------------- LOGIN ----------------

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

    db_user = cursor.fetchone()

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    email, hashed_password = db_user


    if not verify_password(
        user.password,
        hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    token = create_token(email)

    return {
        "token": token
    }



# ---------------- PROTECTED TASK ROUTE ----------------

@app.get("/tasks")
def get_tasks(
    current_user: str = Depends(get_current_user)
):

    return {
        "message": "Protected endpoint accessed",
        "user": current_user
    }