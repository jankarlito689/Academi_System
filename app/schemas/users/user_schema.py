from pydantic import BaseModel, EmailStr
from typing import Optional

# crear usuario
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    rol: str
    academia_id: int

# actualización
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    password_hash: Optional[str] = None
    rol: Optional[str] = None

# salida
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    rol: Optional[str] = None
    academia_id: Optional [int] = None

    class Config:
        from_attributes = True