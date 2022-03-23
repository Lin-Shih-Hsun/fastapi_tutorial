from fastapi import APIRouter
from blog import database, schemas, models
from fastapi import APIRouter, Depends, status, HTTPException# 為了fastapi, 建db, HTTP的status_code, 不需用到了(被HTTPException取代), 可以回傳HTTPException
from sqlalchemy.orm import Session  # 為了建db
from blog.repository import user


router = APIRouter(
    prefix = "/user",   # 可以把所有的router需要用到的都統一prefix，讓code更乾淨
    tags=['Users']   # 可以把所有的router相同的tags都統一在這設定，讓code更乾淨
)
get_db = database.get_db

# request -> request body
# response_model -> the model is responsed
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)