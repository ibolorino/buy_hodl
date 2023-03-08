from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from buy_hodl.api.dependencies import get_db
from buy_hodl import crud, schemas
from buy_hodl.config import get_settings
from buy_hodl.api.v1.core import security
from typing import Any
from datetime import timedelta

settings = get_settings()

router = APIRouter(prefix="/auth")

@router.post("/login", response_model=schemas.Token)
def login_access_token(login_data: schemas.AuthLogin, db: Session = Depends(get_db)) -> Any:
    user = crud.user.authenticate(db, email=login_data.username, password=login_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password.")
    if not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="User is not active.")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }

