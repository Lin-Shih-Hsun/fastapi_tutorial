from fastapi import FastAPI

from blog.routers import authentication
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine) # 只要找到model,就創建"Database"的"Table"!!!

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
