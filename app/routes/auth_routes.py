# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException
from app.controllers.users.auth_controllers import login_user_controller, logout_user_controller
from app.schemas.users.auth_schema import Login, LoginResponse, LogoutResponse
from app.middlewares.session import check_jwt

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=LoginResponse)
async def login(login_data: Login):
    return await login_user_controller(login_data.email,login_data.password,login_data.academia_id)

@router.post("/logout", response_model=LogoutResponse)
async def logout(token_payload: dict = Depends(check_jwt)):
    user_id = token_payload.get("user_id")
    academia_id = token_payload.get("academia_id")

    if user_id is None or academia_id is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    return await logout_user_controller(int(user_id), int(academia_id))