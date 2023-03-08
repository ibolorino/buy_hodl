from .base import CRUDBase
from buy_hodl.models import Asset_Type
from buy_hodl.schemas import AssetTypeCreate, AssetTypeUpdate

class CRUDAssetType(CRUDBase[Asset_Type, AssetTypeCreate, AssetTypeUpdate]):
    pass
    

asset_type = CRUDAssetType(Asset_Type)