from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    # Ensure that the columns in the User model match the fields in UserCreate
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
