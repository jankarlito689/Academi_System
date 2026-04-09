from app.models.users.user_models import get_all_users, get_user_by_id, create_user, update_user, delete_user

def list_users():
    return get_all_users()

def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user.data:
        raise Exception("User not found")
    return user

def create_new_user(data: dict):
    user = create_user(data)
    if not user.data:
        raise Exception("User not found")
    return user

def update_existing_user(user_id: int, data: dict):
    user = update_user(user_id, data)
    if not user.data:
        raise Exception("User not found")
    return user

def delete_existing_user(user_id: int):
    user = delete_user(user_id)
    if not user.data:
        raise Exception("User not found")
    return user