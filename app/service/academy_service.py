from app.models.academy_models import get_all_academias, get_academia_by_id, create_academia, update_academia, delete_academia

def list_academias():
    return get_all_academias()

def get_academia(academia_id: int):
    academia = get_academia_by_id(academia_id)
    if not academia.data:
        raise Exception("Academia not found")
    return academia

def create_new_academia(data: dict):
    academia = create_academia(data)
    if not academia.data:
        raise Exception("Academia not found")
    return academia

def update_existing_academia(academia_id: int, data: dict):
    academia = update_academia(academia_id, data)
    if not academia.data:
        raise Exception("Academia not found")
    return academia

def delete_existing_academia(academia_id: int):
    academia = delete_academia(academia_id)
    if not academia.data:
        raise Exception("Academia not found")
    return academia