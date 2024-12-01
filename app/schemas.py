from pydantic import BaseModel

# User creation schema
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# User response schema
class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy models
