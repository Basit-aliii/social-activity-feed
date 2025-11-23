from pydantic import BaseModel
from datetime import datetime

class ActivityOut(BaseModel):
    id: int
    user_id: int
    action: str
    created_at: datetime

    class Config:
        orm_mode = True
