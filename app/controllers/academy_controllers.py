from app.service.academy_service import list_academias, get_academia, create_new_academia, update_existing_academia, delete_existing_academia
from app.utils.exceptions import not_found, server_error

def get_academias_controller():
    result = list_academias()
    return result.data

def get_academia_controller(academia_id: int):
    academia = get_academia(academia_id)
    if not academia.data:
        not_found("Academia not found")

    return academia.data

def create_academia_controller(data):
    try:
        result = create_new_academia(data.dict())
        return result.data[0]   # Retorna el nuevo usuario creado
    except Exception:
        server_error("Error creating academia")

def update_academia_controller(academia_id: int, data):
    try:
        result = update_existing_academia(academia_id, data.dict(exclude_unset=True))
        return result.data[0]   # Retorna el nuevo usuario creado
    except Exception:
        server_error("Error updating academia")

def delete_academia_controller(academia_id: int):
    result = delete_existing_academia(academia_id)

    if not result.data:
        not_found("Academia not found")

    return {"message": "Academia deleted successfully"}