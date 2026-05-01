from app.models.atletas_models import (
    get_atleta_by_id,
    get_atletas_by_academia_id,
    create_atleta,
    update_atleta,
    delete_atleta
)

from app.utils.exceptions import not_found, bad_request

# ✅ Obtener atleta por ID (validando academia)
async def get_atleta(atleta_id: int, academia_id: int):
    response = get_atleta_by_id(atleta_id, academia_id)

    atleta = response.data

    if not atleta:
        raise not_found("Atleta no encontrado")

    return atleta

# ✅ Listar atletas por academia
async def List_atletas(academia_id: int):
    response = get_atletas_by_academia_id(academia_id)
    return response.data

# ✅ Crear atleta
async def create_new_atleta(atleta_data: dict):
    # 🔹 regla: estado por defecto
    if "estado" not in atleta_data:
        atleta_data["estado"] = "activo"

    # 🔹 validaciones simples
    if atleta_data.get("estado") not in ["activo", "inactivo"]:
        raise bad_request("Estado inválido")

    response = create_atleta(atleta_data)
    if not response.data:
        raise bad_request("Error al crear atleta")

    return response.data[0]


# ✅ Actualizar atleta
async def update_existing_atleta(atleta_id: int, academia_id: int, atleta_data: dict):
    response = get_atleta_by_id(atleta_id, academia_id)
    atleta = response.data

    if not atleta:
        raise not_found("Atleta no encontrado")

    response = update_atleta(atleta_id, atleta_data)
    if not response.data:
        raise not_found("Error al actualizar atleta")
    
    return response.data[0]


# ✅ Eliminar atleta
async def delete_existing_atleta(atleta_id: int, academia_id: int):
    response = get_atleta_by_id(atleta_id, academia_id)
    atleta = response.data

    if not atleta:
        raise not_found("Atleta no encontrado")

    deleted = delete_atleta(atleta_id)
    if not deleted.data:
        raise not_found("Error al eliminar atleta")
    
    return {"message": "Atleta eliminado correctamente"}