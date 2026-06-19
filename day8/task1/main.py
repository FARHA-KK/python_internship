from fastapi import FastAPI, HTTPException

from database import conn, cursor
from models import UserRegister
from auth import hash_password


app = FastAPI()



@app.get("/")
def home():

    return {
        "message": "Auth API"
    }



# Register User
@app.post("/auth/register")
def register(
    user: UserRegister
):

    # check existing email
    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )

    existing_user = cursor.fetchone()


    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


    # convert password to hash
    hashed_password = hash_password(
        user.password
    )


    # store hashed password
    cursor.execute(
        """
        INSERT INTO users(email, hashed_password)
        VALUES (?,?)
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