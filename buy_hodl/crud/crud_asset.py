from .base import CRUDBase
from buy_hodl.models import Asset
from buy_hodl.schemas import AssetCreate, AssetUpdate


class CRUDAsset(CRUDBase[Asset, AssetCreate, AssetUpdate]):
    pass


asset = CRUDAsset(Asset)