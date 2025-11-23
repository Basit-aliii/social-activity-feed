from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.models.follow import Follow
from app.models.user import User
from app.schemas.follow import FollowOut

router = APIRouter()

@router.post("/{user_id}", response_model=FollowOut)
async def follow_user(user_id: int, db: AsyncSession = Depends(get_db)):
    follow = Follow(following_id=user_id)
    db.add(follow)
    await db.commit()
    await db.refresh(follow)
    return follow
