import bcrypt

def encrypt_password(password: str) -> str:
    """
    Encripta la contraseña usando bcrypt.
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        Contraseña encriptada (hash)
    """
    salt = bcrypt.gensalt(rounds=10)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verifica si la contraseña coincide con el hash almacenado.
    
    Args:
        password: Contraseña en texto plano a verificar
        password_hash: Hash de la contraseña almacenada
        
    Returns:
        True si la contraseña coincide, False en caso contrario
    """
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
