from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.models.like import Like
from app.models.post import Post
from app.schemas.like import LikeOut

router = APIRouter()

@router.post("/{post_id}", response_model=LikeOut)
async def like_post(post_id: int, db: AsyncSession = Depends(get_db)):
    post = await db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    like = Like(post_id=post_id)
    db.add(like)
    await db.commit()
    await db.refresh(like)
    return like
