from fastapi import APIRouter
from app.controllers.user_controllers import get_users_controller,get_user_controller, create_user_controller, update_user_controller, delete_user_controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    return get_users_controller()

@router.get("/{user_id}")
def get_user(user_id: int):
    return get_user_controller(user_id)

@router.post("/")
def create_user(data: dict):
    return create_user_controller(data)

@router.put("/{user_id}")
def update_user(user_id: int, data: dict):
    return update_user_controller(user_id, data)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return delete_user_controller(user_id)