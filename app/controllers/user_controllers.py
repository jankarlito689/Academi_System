from fastapi import HTTPException
from app.service.user_service import list_users, get_user, create_new_user, update_existing_user, delete_existing_user

def get_users_controller():
    result = list_users()
    return result.data

def get_user_controller(user_id: int):
    user = get_user(user_id)
    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")

    return user.data
def create_user_controller(data):
    try:
        result = create_new_user(data.dict())
        return result.data[0]   # Retorna el nuevo usuario creado
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

def update_user_controller(user_id: int, data):
    try:
        result = update_existing_user(user_id, data.dict(exclude_unset=True))
        return result.data[0]
    except Exception:
        raise HTTPException(status_code=500, detail="Error updating user")


def delete_user_controller(user_id: int):
    result = delete_existing_user(user_id)

    if not result.data:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}