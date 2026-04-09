# app/utils/jwt_handle.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException
from dotenv import load_dotenv
import os

# cargar variables
load_dotenv()

SECRET_KEY: str = os.getenv("SECRET_KEY", "")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está configurada en el .env")


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Crea un JWT seguro con información del usuario
    """

    to_encode = data.copy()
    # ⏳ Expiración
    expire = datetime.utcnow() + (expires_delta or timedelta(hours=8))
    # 📌 Claims estándar
    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),  # issued at
    })
    # 🔐 Generar token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")