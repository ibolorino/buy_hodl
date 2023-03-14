from fastapi import APIRouter, Depends, HTTPException
from typing import List, Any
from buy_hodl import schemas, crud, models
from buy_hodl.api.dependencies import get_db, is_admin, is_authenticated
from sqlalchemy.orm import Session


router = APIRouter(prefix="/asset_type")

@router.get("/", response_model=List[schemas.AssetType])
def list_asset_types(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(is_authenticated),
) -> Any:
    asset_types = crud.asset_type.get_multi(db, skip=skip, limit=limit)
    return asset_types

@router.post("/", response_model=schemas.AssetType)
def create_asset_type(
    *,
    db: Session = Depends(get_db),
    asset_type_in: schemas.AssetTypeCreate,
    current_user: models.User = Depends(is_admin),
) -> Any:
    asset_type = crud.asset_type.create(db=db, obj_in=asset_type_in)
    return asset_type

@router.get("/{id}", response_model=schemas.AssetType)
def read_asset_type(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: models.User = Depends(is_authenticated),
) -> Any:
    asset_type = crud.asset_type.get(db=db, id=id)
    if not asset_type:
        raise HTTPException(status_code=404, detail="Asset Type not found")
    return asset_type

@router.put("/{id}", response_model=schemas.AssetType)
def update_asset_type(
    *,
    db: Session = Depends(get_db),
    id: int,
    asset_type_in: schemas.AssetTypeUpdate,
    current_user: models.User = Depends(is_admin),
) -> Any:
    asset_type = crud.asset_type.get(db=db, id=id)
    if not asset_type:
        raise HTTPException(status_code=404, detail="Asset Type not found")
    asset_type = crud.asset_type.update(db=db, db_obj=asset_type, obj_in=asset_type_in)
    return asset_type

@router.delete("/{id}", response_model=schemas.AssetType)
def delete_asset_type(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: models.User = Depends(is_admin),
) -> Any:
    asset_type = crud.asset_type.get(db=db, id=id)
    if not asset_type:
        raise HTTPException(status_code=404, detail="Asset Type not found")
    asset_type = crud.asset_type.remove(db=db, id=id)
    return asset_type