from fastapi import APIRouter, Depends, HTTPException
from typing import List, Any
from buy_hodl import schemas, crud, models
from buy_hodl.api.dependencies import get_db, is_authenticated, is_admin
from sqlalchemy.orm import Session


router = APIRouter(prefix="/asset")

@router.get("/", response_model=List[schemas.Asset])
def list_asset(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(is_authenticated)
) -> Any:
    assets = crud.asset.get_multi(db, skip=skip, limit=limit)
    return assets

@router.post("/", response_model=schemas.Asset)
def create_asset(
    *,
    db: Session = Depends(get_db),
    asset_in: schemas.AssetCreate,
    current_user: models.User = Depends(is_admin),
) -> Any:
    asset = crud.asset.create(db=db, obj_in=asset_in)
    return asset

@router.get("/{id}", response_model=schemas.Asset)
def read_asset(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: models.User = Depends(is_authenticated),
) -> Any:
    asset = crud.asset.get(db=db, id=id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@router.put("/{id}", response_model=schemas.Asset)
def update_asset(
    *,
    db: Session = Depends(get_db),
    id: int,
    asset_in: schemas.AssetUpdate,
    current_user: models.User = Depends(is_admin),
) -> Any:
    asset = crud.asset.get(db=db, id=id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    asset = crud.asset.update(db=db, db_obj=asset, obj_in=asset_in)
    return asset

@router.delete("/{id}", response_model=schemas.Asset)
def delete_asset(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: models.User = Depends(is_admin),
) -> Any:
    asset = crud.asset.get(db=db, id=id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    asset = crud.asset.remove(db=db, id=id)
    return asset