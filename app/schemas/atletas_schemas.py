from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from datetime import date


class AtletaCreate(BaseModel):
    academia_id: int
    nombre: str
    email: EmailStr
    telefono: str
    fecha_nacimiento: date
    estado: Literal["activo", "inactivo"]
    tipo: Literal["recreativo", "competitivo"]
    categoria: str
    

class AtletaUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    estado: Optional[Literal["activo", "inactivo"]] = None
    tipo: Optional[Literal["recreativo", "competitivo"]] = None
    categoria: Optional[str] = None

class AtletaResponse(BaseModel):
    id: int
    academia_id: int
    nombre: str
    email: EmailStr
    telefono: str
    fecha_nacimiento: date
    estado: Literal["activo", "inactivo"]
    tipo: Literal["recreativo", "competitivo"]
    categoria: str

    class Config:
        from_attributes = True