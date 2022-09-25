from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from app.schemas import UserDisplay
from app.schemas.comment import Comment


class PostBase(BaseModel):
    image_url: Optional[str] = None
    image_url_type: Optional[str] = None
    caption: Optional[str] = None
    creator_id: Optional[int] = None


class PostCreate(PostBase):
    pass


class PostDisplay(BaseModel):
    id: int
    image_url: Optional[str] = None
    image_url_type: Optional[str] = None
    caption: Optional[str] = None
    created_at: Optional[datetime]
    user: UserDisplay
    comments: List[Comment]

    class Config:
        orm_mode = True
