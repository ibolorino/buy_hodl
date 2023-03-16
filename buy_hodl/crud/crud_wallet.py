from .base import CRUDBase
from buy_hodl.models import Wallet
from buy_hodl.schemas import WalletCreate, WalletUpdate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException


class CRUDWallet(CRUDBase[Wallet, WalletCreate, WalletUpdate]):
    def get_multi(
        self, db: Session, *, user_id: int
    ) -> List[Wallet]:
        return db.query(self.model).filter(Wallet.user_id == user_id).all()

    def create(
        self, db: Session, *, obj_in: WalletCreate, user_id: int
    ) -> Wallet:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        try:
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except IntegrityError as ie:
            db.rollback()
            if ie.orig.diag.constraint_name == "wallet_unique_asset_user_key":
                raise HTTPException(status_code=400, detail="You already have this asset in your wallet.")
            raise HTTPException(status_code=400, detail=str(ie))

    def get_by_owner(
        self, db: Session, id: int, user_id: int
    ) -> Optional[Wallet]:
        return db.query(Wallet).filter(Wallet.id == id, Wallet.user_id == user_id).first()

wallet = CRUDWallet(Wallet)