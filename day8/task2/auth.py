from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uuid


# password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# store tokens here
sessions = {}


# create password hash
def hash_password(password: str):
    return pwd_context.hash(password)


# check password
def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# create login token
def create_token(email: str):

    token = str(uuid.uuid4())

    sessions[token] = email

    return token


# security for swagger
security = HTTPBearer()


# protected route checker
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    email = sessions.get(token)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return email