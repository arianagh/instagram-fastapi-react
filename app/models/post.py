import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Post(Base):

    __tablename__ = "posts"
    id = Column(
        Integer, primary_key=True, index=True
    )

    image_url = Column(String(255), nullable=True)
    image_url_type = Column(String(255), nullable=True)
    caption = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )
    user = relationship("User", back_populates="posts")
