from fastapi import APIRouter, Depends
from app.controllers.atletas_controllers import (
    get_atletas_controller,
    get_atleta_controller,
    create_atleta_controller, 
    update_atleta_controller,
    delete_atleta_controller
)
from app.schemas.atletas_schemas import AtletaCreate, AtletaUpdate, AtletaResponse
from app.middlewares.session import check_jwt

router = APIRouter(prefix="/atletas", tags=["Atletas"])


# ✅ GET ALL
@router.get("/", response_model=list[AtletaResponse])
async def get_atletas(user=Depends(check_jwt)):
    academia_id = user["academia_id"]
    return await get_atletas_controller(academia_id)


# ✅ GET ONE
@router.get("/{atleta_id}", response_model=AtletaResponse)
async def get_atleta(atleta_id: int, user=Depends(check_jwt)):
    academia_id = user["academia_id"]
    return await get_atleta_controller(atleta_id, academia_id)


# ✅ CREATE
@router.post("/", response_model=AtletaResponse)
async def create_atleta(data: AtletaCreate, user=Depends(check_jwt)):
    academia_id = user["academia_id"]

    # 🔐 evitar que el cliente manipule academia_id
    payload = data.model_dump(mode="json")
    payload["academia_id"] = academia_id

    return await create_atleta_controller(payload)


# ✅ UPDATE
@router.put("/{atleta_id}", response_model=AtletaResponse)
async def update_atleta(atleta_id: int, data: AtletaUpdate, user=Depends(check_jwt)):
    academia_id = user["academia_id"]

    return await update_atleta_controller(
        atleta_id,
        academia_id,
        data
    )


# ✅ DELETE
@router.delete("/{atleta_id}")
async def delete_atleta(atleta_id: int, user=Depends(check_jwt)):
    academia_id = user["academia_id"]

    return await delete_atleta_controller(atleta_id, academia_id)