from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = "users"
    id = Column(
        Integer, primary_key=True, index=True
    )
    username = Column(String(255), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    posts = relationship("Post", back_populates="user")
