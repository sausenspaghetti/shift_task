from fastapi import Response, \
    status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from passlib.context import CryptContext
from typing import Optional

from .. import models, schema, utils, oauth2
from ..database import  get_db
# from .. import app


router = APIRouter(
    prefix='/users',
    tags=['UserEmployee']
)



# Only admin can change
@router.post('/', status_code=status.HTTP_201_CREATED,  response_model=schema.UserOut)
def create_user(
        user: schema.UserCreate, 
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.UserEmployee(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}',  response_model=schema.UserOut) 
def get_user(
        id: int, 
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)):
    
    user = db.query(models.UserEmployee).filter(models.UserEmployee.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    
    return user