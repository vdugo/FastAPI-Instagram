from fastapi import FastAPI, status, HTTPException
from fastapi.staticfiles import StaticFiles

from auth import authentication
from db import models
from db.database import engine
from routers import user, post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)

@app.get('/')
def home_page():
    return {"message": "this is the homepage"}

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')