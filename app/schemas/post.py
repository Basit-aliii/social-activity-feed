from pydantic import BaseModel

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
