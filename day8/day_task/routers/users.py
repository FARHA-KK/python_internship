from fastapi import APIRouter, HTTPException

from database import cursor, conn

from schemas import UserCreate

from auth import (
    hash_password,
    verify_password,
    create_token
)



router = APIRouter(
    prefix="/auth",
    tags=["Users"]
)



# Register

@router.post("/register")
def register(
    user: UserCreate
):

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
        INSERT INTO users
        (email,hashed_password)
        VALUES(?,?)
        """,
        (
            user.email,
            hashed
        )
    )


    conn.commit()


    return {
        "message":"registered"
    }





# Login

@router.post("/login")
def login(
    user: UserCreate
):

    cursor.execute(
        """
        SELECT email,hashed_password
        FROM users
        WHERE email=?
        """,
        (user.email,)
    )


    data = cursor.fetchone()


    if not data:

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





# Current user

@router.get("/me")
def get_me(
    user: str
):

    return {
        "email": user
    }