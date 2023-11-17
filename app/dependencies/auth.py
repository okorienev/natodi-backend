from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError

from app.settings import settings


auth_scheme = HTTPBearer()


def get_user_from_token_or_abort(authorization: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> str:

    if not authorization.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    token = authorization.credentials.replace("Bearer ", "")
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
    except JWTError as error:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(error)
        ) from error
    
    if payload.get("sub") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )

    return token
