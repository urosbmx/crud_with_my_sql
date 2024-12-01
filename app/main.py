from fastapi import Depends, FastAPI,HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal  # Absolute import
from . import crud
from . import schemas

# Initialize the FastAPI application
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to delete the user
    deleted = crud.delete_user_by_id(db=db, user_id=user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": f"User {user_id} deleted successfully."}