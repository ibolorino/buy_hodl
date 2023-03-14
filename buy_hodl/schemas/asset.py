from pydantic import BaseModel
from typing import Optional
from decimal import Decimal


# Shared properties
class AssetBase(BaseModel):
    name: Optional[str] = None
    ticker: Optional[str] = None
    current_price: Optional[Decimal] = None
    asset_type_id: int


# Properties to receive on asset_type creation
class AssetCreate(AssetBase):
    name: str
    ticker: str


# Properties to receive on asset_type update
class AssetUpdate(AssetBase):
    pass


# Properties shared by models stored in DB
class AssetInDBBase(AssetBase):
    id: int
    name: str
    ticker: str
    current_price: Optional[Decimal]
    asset_type_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Asset(AssetInDBBase):
    pass


# Properties properties stored in DB
class AssetIdDB(AssetInDBBase):
    pass