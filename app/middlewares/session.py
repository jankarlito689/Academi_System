#middlaware/session.py
from fastapi import Request, HTTPException, status
from app.utils.jwt_handle import verify_token


async def check_jwt(request: Request):
    """
    Middleware/Dependency para validar JWT en rutas protegidas
    """

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no proporcionado"
        )

    try:
        # Formato esperado: Bearer <token>
        scheme, token = auth_header.split()

        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Formato de token inválido"
            )

        payload = verify_token(token)

        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

        return payload  # 👈 importante (lo puedes usar en la ruta)

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token mal formado"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error al validar token"
        )
