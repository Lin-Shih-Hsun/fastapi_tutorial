from passlib.context import CryptContext # 為了加密密碼

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")   # 加密密碼所需

class Hash():
    def brtypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)