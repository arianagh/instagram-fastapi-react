import datetime

from sqlalchemy import Column, String, Integer,\
    Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Comment(Base):
    __tablename__ = "comments"
    id = Column(
        Integer, primary_key=True, index=True
    )
    username = Column(String(255), nullable=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    post_id = Column(
        Integer,
        ForeignKey("posts.id"),
        nullable=True,
    )
    post = relationship("Post", back_populates="comments")
