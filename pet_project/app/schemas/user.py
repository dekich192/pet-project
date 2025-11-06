from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from uuid import UUID as UUID4

# User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)

class UserInDB(UserBase):
    id: UUID4
    is_active: bool
    
    class Config:
        from_attributes = True

class UserResponse(UserInDB):
    pass

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: str | None = None

# Worker schemas
class WorkerBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)

class WorkerCreate(WorkerBase):
    pass

class WorkerResponse(WorkerBase):
    id: UUID4
    
    class Config:
        from_attributes = True
