from fastapi import APIRouter, Depends, HTTPException
from buy_hodl import schemas, crud, models
from typing import List, Any
from buy_hodl.api.dependencies import get_db, is_authenticated, is_admin
from sqlalchemy.orm import Session



router = APIRouter(prefix="/wallet")

@router.get("/", response_model=List[schemas.Wallet])
def list_wallet(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(is_authenticated)
) -> Any:
    wallets = crud.wallet.get_multi(db, user_id=current_user.id)
    return wallets

@router.post("/", response_model=schemas.Wallet)
def list_wallet(
    *,
    db: Session = Depends(get_db),
    wallet_in: schemas.WalletCreate,
    current_user: models.User = Depends(is_authenticated)
) -> Any:
    wallet = crud.wallet.create(db=db, obj_in=wallet_in, user_id=current_user.id)
    return wallet