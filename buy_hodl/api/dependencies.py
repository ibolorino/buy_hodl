from typing import Generator
from buy_hodl.db.session import SessionLocal
from buy_hodl import models, schemas, crud
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from buy_hodl.config import get_settings
from sqlalchemy.orm import Session
from pydantic import ValidationError

settings = get_settings()

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail="Could not validate credentials"
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

def is_authenticated(
    current_user: models.User = Depends(get_current_user)
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(
            status_code=400,
            detail="Inactive User"
        )
    return current_user

def is_admin(
    current_user: models.User = Depends(get_current_user)
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
                status_code=400,
                detail="The user doesn't have enough privileges"
            )
    return current_user