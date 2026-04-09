from pydantic import BaseModel, EmailStr
from typing import Optional

class Login(BaseModel):
    email: EmailStr
    password: str
    academia_id: int

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    academia_id: int
    email: EmailStr
    rol: str