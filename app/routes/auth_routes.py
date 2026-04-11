# app/routes/auth_routes.py
from fastapi import APIRouter
from app.controllers.users.auth_controllers import login_user_controller
from app.schemas.users.auth_schema import Login, LoginResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=LoginResponse)
async def login(login_data: Login):
    return await login_user_controller(login_data.email,login_data.password,login_data.academia_id)