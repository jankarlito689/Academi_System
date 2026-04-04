#exceptions.py
from fastapi import HTTPException,status


def not_found(message: str = "Resource not found"):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    )

def server_error(message: str = "Internal server error"):
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=message
    )

def bad_request(message: str = "Bad request"):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message
    )