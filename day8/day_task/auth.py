from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Header
import uuid
import os
from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")


pwd_context = CryptContext(
    schemes=["bcrypt"]
)


# token storage
sessions = {}



def hash_password(password):

    return pwd_context.hash(password)



def verify_password(
    plain,
    hashed
):

    return pwd_context.verify(
        plain,
        hashed
    )



def create_token(email):

    token = str(uuid.uuid4())

    sessions[token] = email

    return token



# protected route checker

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException


security = HTTPBearer()


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