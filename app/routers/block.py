from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.models.block import Block
from app.schemas.block import BlockOut

router = APIRouter()

@router.post("/{blocked_id}", response_model=BlockOut)
async def block_user(blocked_id: int, db: AsyncSession = Depends(get_db)):
    block = Block(blocked_id=blocked_id)
    db.add(block)
    await db.commit()
    await db.refresh(block)
    return block
