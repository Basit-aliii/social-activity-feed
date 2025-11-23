from pydantic import BaseModel

class BlockBase(BaseModel):
    blocked_id: int

class BlockOut(BaseModel):
    id: int
    blocker_id: int
    blocked_id: int

    class Config:
        orm_mode = True
