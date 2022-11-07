from sqlalchemy.orm.session import Session

from db.hashing import Hash
from .models import DbUser
from routers.schemas import UserBase

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        # store the hashed password
        password = Hash.bcrypt(request.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user