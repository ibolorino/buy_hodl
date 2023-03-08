from fastapi import APIRouter, Depends
from typing import List, Any
from buy_hodl import schemas, crud
from buy_hodl.api.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/asset_type")

@router.get("/", response_model=List[schemas.AssetType])
def list_asset_types(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    asset_types = crud.asset_type.get_multi(db, skip=skip, limit=limit)
    return asset_types

@router.post("/", response_model=schemas.AssetType)
def create_asset_type(
    *,
    db: Session = Depends(get_db),
    asset_type_in: schemas.AssetTypeCreate
) -> Any:
    asset_type = crud.asset_type.create(db=db, obj_in=asset_type_in)
    return asset_type