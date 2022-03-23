from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# INSTRUCTION!!!
'''
@app.get('/')
def abc():
    return {'data': {'name': 'Brian'}}
'''
# ('/') is Path
# get is Operation(or method)(eg. get, post, delete, put)
# def abc(): ... is Path Operation Function
# @app is Path Operation Decorator

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpubished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments of blog with id = id
    return {'data': {'1','2'}}

# post是另一種Operation(or method),可以創造新的('/blog')
# "Request Body" : the thing that you need to send data from client(browser) to your API.
# to declare a request body needed use Pydantic models

class Blog(BaseModel):  # 需要from pydentic import BaseModel
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')  # 注意，post沒辦法從URL直接下，可以藉由fastapi的swaggerUI(localhost:8000/docs)
def create_blog(blog: Blog): # blog is the request body
    return {'data': f'Blog is created with title as {blog.title}'}

# If you want to change the port from "8000 -> 9000"
# import uvicorn
# if __name__ == "__main__": 
#     uvicorn.run(app, host = "127.0.0.1", port='9000')