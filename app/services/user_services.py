from typing import Optional

from app.core.security import get_password_hash, verify_password
from app.services.base import BaseServices
from sqlalchemy.orm import Session
from pydantic.types import UUID4
from app import models, schemas, services


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

    # def authenticate(
    #     self, db: Session, *, email: str, password: str
    # ) -> Optional[models.User]:
    #     user = self.get_by_email(db, email=email)
    #     if not user:
    #         return None
    #     if not verify_password(password, user.hashed_password):
    #         return None
    #     return user

    def get(self, db: Session, id: UUID4) -> Optional[models.User]:
        user = db.query(models.User).filter(models.User.id == id).first()
        return user


user = UserServices(models.User)
