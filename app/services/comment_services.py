from sqlalchemy.orm import Session

from app import models, schemas
from app.services.base import BaseServices


class CommentServices(
    BaseServices
    [
        models.comment,
        schemas.CommentCreate,
    ]
):

    def create(
            self,
            db: Session,
            *,
            obj_in: schemas.CommentCreate
    ) -> models.Comment:
        new_comment = models.Comment(
            username=obj_in.username,
            text=obj_in.text,
            post_id=obj_in.post_id
        )
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment

    def get_all(
            self,
            db: Session,
            post_id: int
    ):
        return db.query(self.model).filter(models.Comment.post_id == post_id).all()


comment = CommentServices(models.Comment)
