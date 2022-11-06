from fastapi import FastAPI, status, HTTPException

from db import models
from db.database import engine

app = FastAPI()

@app.get('/')
def home_page():
    return {"message": "this is the homepage"}

models.Base.metadata.create_all(engine)