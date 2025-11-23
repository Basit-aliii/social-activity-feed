from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db import get_db
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate, PostOut
from app.utils.auth import create_access_token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter()

@router.post("/", response_model=PostOut)
async def create_post(payload: PostCreate, db: AsyncSession = Depends(get_db)):
    post = Post(content=payload.content)
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post
