from typing import List
from fastapi import APIRouter, Depends, status, HTTPException# 為了fastapi, 建db, HTTP的status_code, 不需用到了(被HTTPException取代), 可以回傳HTTPException
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session  # 為了建db
from blog.repository import blog


router = APIRouter(
    prefix = "/blog",   # 可以把所有的router需要用到的都統一prefix，讓code更乾淨
    tags=['Blogs']   # 可以把所有的router相同的tags都統一在這設定，讓code更乾淨
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

# 可以創建新的title, body in swaggerAPI，並且給予id
@router.post('/', status_code=status.HTTP_201_CREATED) # status有各種http的status code
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):   # db:透過fastAPI的Depends抓db進來
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):   # 需要request body才能create或update
    return blog.update(id, request, db)

# 可以看到所有在db的資料
# @router.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)    # response_model就是你要回應的model(pydantic)，可以設置隱藏id的model(或不想顯示的內容)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)