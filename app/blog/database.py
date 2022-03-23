# create database connection : (1)engine (2)sessionmaker (3)declarative_base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database engine

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args = {
    "check_same_thread": False})

# sessionmaker

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# declarative_base

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()