from fastapi import FastAPI, status, HTTPException

from db import models
from db.database import engine
from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get('/')
def home_page():
    return {"message": "this is the homepage"}

models.Base.metadata.create_all(engine)