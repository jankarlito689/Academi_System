from fastapi import APIRouter
from app.controllers.academy_controllers import ( 
    get_academia_controller, 
    get_academias_controller, 
    create_academia_controller, 
    update_academia_controller, 
    delete_academia_controller
)
from app.schemas.academy_schema import AcademyCreate, AcademyUpdate, AcademyResponse
from typing import List

router = APIRouter(prefix="/academias", tags=["Academias"])

@router.get("/", response_model=List[AcademyResponse])
def get_academias():
    return get_academias_controller()

@router.get("/{academia_id}", response_model=AcademyResponse)
def get_user(academia_id: int):
    return get_academia_controller(academia_id)

@router.post("/", response_model=AcademyResponse)
def create_academia(academia: AcademyCreate):
    return create_academia_controller(academia)

@router.put("/{academia_id}", response_model=AcademyResponse)
def update_academia(academia_id: int, data: AcademyUpdate):
    return update_academia_controller(academia_id, data)

@router.delete("/{academia_id}")
def delete_academia(academia_id: int):
    return delete_academia_controller(academia_id)