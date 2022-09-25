from typing import Optional

from fastapi import HTTPException
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from starlette import status

from app import models, schemas
from app.core.security import get_password_hash
from app.services.base import BaseServices


class PostServices(
    BaseServices
    [
        models.Post,
        schemas.PostBase,
    ]
):

    def create(
            self,
            db: Session,
            *,
            obj_in: schemas.PostCreate
    ) -> models.Post:
        new_post = models.Post(
            image_url=obj_in.image_url,
            image_url_type=obj_in.image_url_type,
            caption=obj_in.caption,
            user_id=obj_in.creator_id
        )
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post

    def remove(
            self,
            db: Session,
            *,
            id: int,
            user_id: int
    ):
        post = db.query(self.model).filter(models.Post.id == id).first()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Post with id {id} not found')
        if post.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail='Only post creator can delete post')

        db.delete(post)
        db.commit()
        return

    # def get(self, db: Session, id: UUID4) -> Optional[models.User]:
    #     user = db.query(models.User).filter(models.User.id == id).first()
    #     return user


post = PostServices(models.Post)
