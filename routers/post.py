from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_post
from .schemas import PostBase, PostDisplay

router = APIRouter(
    prefix='/post',
    tags=['post']
)

image_url_types = ['absolute', 'relative']

@router.post('/', response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                            detail="parameter image_url_type can only take values 'absolute' or 'relative'")
    return db_post.create(db, request)

@router.get('/all', response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    pass