from fastapi import APIRouter, Depends, Path
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from app.cruds.user import user_crud
from app.dependencies import get_db
from app.schemas.user import CreateUserSchema

router = APIRouter(prefix="/user")


@router.get("/{user_id}", response_class=PlainTextResponse)
def get(user_id: int = Path(), db: Session = Depends(get_db)):
    user_crud.get(db=db, id=user_id)
    return PlainTextResponse(content="OK")


@router.post("", response_class=PlainTextResponse)
def create(user_in: CreateUserSchema, db: Session = Depends(get_db)):
    user_crud.create(db=db, obj_in=user_in)
    return PlainTextResponse(content="OK")

