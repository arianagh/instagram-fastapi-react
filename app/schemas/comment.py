from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    username: Optional[str] = None
    text: Optional[str] = None
    post_id: int


class CommentCreate(CommentBase):
    pass


class Comment(BaseModel):
    username: Optional[str] = None
    text: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
