from typing import Optional

from pydantic import BaseModel


class UserAuth(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
