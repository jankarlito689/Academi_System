from fastapi import HTTPException
from app.service.user_service import list_users, get_user, create_new_user, update_existing_user, delete_existing_user

def get_users_controller():
    return list_users()

def get_user_controller(user_id: int):
    try:
        return get_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
def create_user_controller(data: dict):
    try:
        return create_new_user(data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

def update_user_controller(user_id: int, data: dict):
    try:
        return update_existing_user(user_id, data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

def delete_user_controller(user_id: int):
    try:
        return delete_existing_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))