from app.models.users.user_models import get_user_by_email_academia
from app.utils.jwt_handle import create_access_token
from app.utils.crypt_handle import verify_password
from fastapi import HTTPException
from typing import Any, Dict, Optional, cast

async def login_user(email: str, password: str, academia_id: int) -> Dict[str, Any]:
    """
    Autentica un usuario y retorna un token JWT.
    """
    try:
        # Buscar usuario por email y academia
        user_result = get_user_by_email_academia(email, academia_id)

        user: Optional[Dict[str, Any]] = cast(Optional[Dict[str, Any]], user_result.data)

        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Verificar contraseña
        if not verify_password(password, user["password_hash"]):
            raise HTTPException(status_code=404, detail="Credenciales incorrectas")
        
        # Crear token
        token_data = {
            "user_id": str(user["id"]),
            "email": user["email"],
            "academia_id": user["academia_id"],
            "rol": user["rol"]
        }
        access_token = create_access_token(token_data)

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    except Exception as e:
        raise Exception(f"Error en login: {str(e)}")

async def logout_user(user_id: int, academia_id: int) -> Dict[str, str]:
    """
    Realiza el logout de un usuario.
    Recibe el user_id y academia_id para validar que el token pertenece al usuario correcto.
    """
    try:
        # Aquí puede ir lógica adicional como:
        # - Guardar en blacklist de tokens
        # - Registrar en logs del sistema
        # - Limpiar sesiones activas
        
        return {
            "message": "Sesión cerrada exitosamente"
        }
    except Exception as e:
        raise Exception(f"Error en logout: {str(e)}")
