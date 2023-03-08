from pydantic import BaseModel
from typing import Optional


# Shared properties
class AssetTypeBase(BaseModel):
    name: Optional[str] = None


# Properties to receive on asset_type creation
class AssetTypeCreate(AssetTypeBase):
    name: str


# Properties to receive on asset_type update
class AssetTypeUpdate(AssetTypeBase):
    pass


# Properties shared by models stored in DB
class AssetTypeInDBBase(AssetTypeBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class AssetType(AssetTypeInDBBase):
    pass


# Properties properties stored in DB
class AssetTypeIdDB(AssetTypeInDBBase):
    pass