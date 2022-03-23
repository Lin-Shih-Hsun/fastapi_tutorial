# 用來擋住看是否有權限，必須輸入正確的email與password才可以得到access_token再進行後續的動作
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from blog import schemas, database, models, JWTtoken
from blog.hashing import Hash
from sqlalchemy.orm import Session  # 為了建db

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()  # login帳號要用使用者的email
    if not user:  # 是否有該user
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):  # password是否正確
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")
    
    access_token = JWTtoken.create_access_token(data={"sub": user.email})  # if everything is fine, 創建token藉由傳送的email_id
    return {"access_token": access_token, "token_type": "bearer"}