from typing import Optional

from sqlalchemy.orm import Session

from app import models, schemas
from app.core.security import get_password_hash
from app.services.base import BaseServices


class UserServices(
    BaseServices
    [
        models.User,
        schemas.UserCreate,
    ]
):

    def register(
            self,
            db: Session,
            *,
            obj_in: schemas.UserCreate
    ) -> models.User:
        db_obj = models.User(
            username=obj_in.username,
            email=obj_in.email,
            password=get_password_hash(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_email(
            self, db: Session, *, email: str
    ) -> Optional[models.User]:
        return db.query(self.model).filter(models.User.email == email).first()

    def get_user_by_username(
            self,
            db: Session,
            *,
            username: str
    ) -> Optional[models.User]:
        user = db.query(self.model).filter(models.User.username == username).first()
        return user


user = UserServices(models.User)
