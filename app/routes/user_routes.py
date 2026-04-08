from fastapi import APIRouter
from app.controllers.users.user_controllers import (
    get_users_controller,
    get_user_controller, 
    create_user_controller, 
    update_user_controller, 
    delete_user_controller
)
from app.schemas.users.user_schema import UserCreate, UserUpdate, UserResponse
from typing import List


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def get_users():
    return get_users_controller()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return get_user_controller(user_id)

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate):
    return create_user_controller(data)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate):
    return update_user_controller(user_id, data)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return delete_user_controller(user_id)