from pydantic import BaseModel, EmailStr
from typing import Optional

class AcademyCreate(BaseModel):
    nombre: str
    email: EmailStr
    phone: str
    direccion: str

class AcademyUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    direccion: Optional[str] = None

class AcademyResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    phone: str
    direccion: str

    class Config:
        from_attributes = True
