#controllers/user_controllers.py
from app.service.users.user_service import list_users, get_user, create_new_user, update_existing_user, delete_existing_user
from app.service.users.auth_service import login_user
from app.utils.exceptions import not_found,server_error

def get_users_controller():
    result = list_users()
    return result.data

def get_user_controller(user_id: int):
    user = get_user(user_id)
    if not user.data:
        not_found("User not found")

    return user.data

def create_user_controller(data):
    try:
        result = create_new_user(data.dict())
        return result.data[0]   # Retorna el nuevo usuario creado
    except Exception:
        server_error("Error creating user")

def update_user_controller(user_id: int, data):
    try:
        result = update_existing_user(user_id, data.dict(exclude_unset=True))
        return result.data[0]
    except Exception:
        server_error("Error updating user")


def delete_user_controller(user_id: int):
    result = delete_existing_user(user_id)

    if not result.data:
        not_found("User not found")

    return {"message": "User deleted successfully"}
