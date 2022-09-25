from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr


class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserDisplay(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True