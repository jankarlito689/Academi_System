# app/controllers/users/auth_controllers.py
from app.service.users.auth_service import login_user
from app.utils.exceptions import server_error
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

async def login_user_controller(email: str, password: str, academia_id: int):
    try:
        login_user_result = await login_user(email, password, academia_id)
        return login_user_result
    except HTTPException:
        raise  # ✅ Re-lanzar 404 de "usuario no encontrado" sin envolver
    except Exception as e:
        server_error(f"Error logging in user: {str(e)}")