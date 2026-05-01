from app.service.atletas_services import ( 
    List_atletas, 
    get_atleta, 
    create_new_atleta, 
    update_existing_atleta, 
    delete_existing_atleta,
    search_atletas
)
from app.utils.exceptions import not_found, server_error

# ✅ GET atletas por academia
async def get_atletas_controller(academia_id: int):
    try:
        return await List_atletas(academia_id)
    except Exception as e:
        raise server_error(f"Error fetching atletas: {str(e)}")

# ✅ GET ONE
async def get_atleta_controller(atleta_id: int, academia_id: int):
    try: 
        return await get_atleta(atleta_id, academia_id)
    except Exception as e:
        raise not_found(f"Atleta not found: {str(e)}")

# ✅ SEARCH
async def search_atletas_controller(nombre: str, academia_id: int):
    try:
        return await search_atletas(nombre, academia_id)
    except Exception as e:
        raise not_found(f"Atletas not found: {str(e)}")

# ✅ CREATE
async def create_atleta_controller(data):
    try:
        return await create_new_atleta(data)
    except Exception as e:
        raise server_error(f"Error creating atleta: {str(e)}")

# ✅ UPDATE
async def update_atleta_controller(atleta_id: int, academia_id: int, data):
    try:
        return await update_existing_atleta(
            atleta_id, 
            academia_id, 
            data.model_dump(exclude_unset=True)
        )
    except Exception as e:
        raise not_found(f"Atleta not found: {str(e)}")

# ✅ DELETE
async def delete_atleta_controller(atleta_id: int, academia_id: int):
    try:
        await delete_existing_atleta(atleta_id, academia_id)
        return {"message": "Atleta deleted successfully"}
    except Exception as e:
        raise not_found(f"Atleta not found: {str(e)}")