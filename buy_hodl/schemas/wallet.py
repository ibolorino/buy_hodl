from pydantic import BaseModel
from typing import Optional


class WalletBase(BaseModel):
    quantity: Optional[int] = None
    quarantine: Optional[bool] = None
    asset_id: Optional[int] = None


class WalletCreate(WalletBase):
    asset_id: int


class WalletUpdate(WalletBase):
    pass


class WalletInDBBase(WalletBase):
    id: int
    quantity: Optional[int]
    quarantine: Optional[bool]
    asset_id: int
    user_id: int

    class Config:
        orm_mode = True


class Wallet(WalletInDBBase):
    pass


class WalletInDB(WalletInDBBase):
    pass