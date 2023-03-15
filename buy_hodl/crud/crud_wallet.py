from .base import CRUDBase
from buy_hodl.models import Wallet
from buy_hodl.schemas import WalletCreate, WalletUpdate
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder


class CRUDWallet(CRUDBase[Wallet, WalletCreate, WalletUpdate]):
    def get_multi(
        self, db: Session, *, user_id: int
    ) -> List[Wallet]:
        return db.query(self.model).filter(Wallet.user_id == user_id).all()

    def create(
        self, db: Session, *, obj_in: WalletCreate, user_id: int
    ) -> Wallet:
        obj_in_data = jsonable_encoder(obj_in)
        print("######################", obj_in_data)
        print("######################", user_id)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

wallet = CRUDWallet(Wallet)