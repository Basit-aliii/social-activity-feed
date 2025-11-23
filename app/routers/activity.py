from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db import get_db
from app.models.activity import Activity
from app.schemas.activity import ActivityOut

router = APIRouter()

@router.get("/", response_model=list[ActivityOut])
async def get_activities(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Activity).order_by(Activity.created_at.desc()))
    activities = result.scalars().all()
    return activities
