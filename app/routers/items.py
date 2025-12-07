from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/", response_model=schemas.Item)
def create_new_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@router.get("/", response_model=list[schemas.Item])
def get_all_items(db: Session = Depends(get_db)):
    return crud.get_items(db)
