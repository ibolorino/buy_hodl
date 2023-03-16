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

@router.put("/{id}", response_model=schemas.Wallet)
def update_wallet(
    *,
    db: Session = Depends(get_db),
    id: int,
    wallet_in: schemas.WalletUpdate,
    current_user: models.User = Depends(is_authenticated),
) -> Any:
    wallet = crud.wallet.get_by_owner(db=db, id=id, user_id=current_user.id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Asset not found in Wallet")
    wallet = crud.wallet.update(db=db, db_obj=wallet, obj_in=wallet_in)
    return wallet

@router.delete("/{id}", response_model=schemas.Wallet)
def delete_wallet(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: models.User = Depends(is_authenticated),
) -> Any:
    wallet = crud.wallet.get_by_owner(db=db, id=id, user_id=current_user.id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Asset not found in Wallet")
    wallet = crud.wallet.remove(db=db, id=id)
    return wallet
