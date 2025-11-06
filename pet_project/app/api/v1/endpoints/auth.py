from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from ....database import get_async_db
from ....models.user import User
from ....schemas.user import Token, UserCreate, UserResponse
from ....core.security import (
    get_password_hash,
    create_access_token,
    verify_password,
    create_refresh_token
)
from ....config import get_settings

router = APIRouter()
settings = get_settings()

@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_async_db)
):
    # This is a simplified version. In a real app, you would verify the user in the database
    if form_data.username != "admin" or form_data.password != "password":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        subject=form_data.username, expires_delta=access_token_expires
    )
    
    refresh_token = create_refresh_token(subject=form_data.username)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "refresh_token": refresh_token
    }

@router.post("/register", response_model=UserResponse)
async def register_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_async_db)
):
    # Check if user already exists
    # In a real app, you would check the database
    if user_in.username == "admin":
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    # Create new user (in a real app, you would save to database)
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password)
    )
    
    # db.add(user)
    # await db.commit()
    # await db.refresh(user)
    
    return user
