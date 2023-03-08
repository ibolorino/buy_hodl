from fastapi import APIRouter, Depends
from typing import List, Any
from buy_hodl import schemas, crud
from buy_hodl.api.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/asset")

@router.get("/", response_model=List[schemas.Asset])
def list_asset_types(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    assets = crud.asset.get_multi(db, skip=skip, limit=limit)
    return assets