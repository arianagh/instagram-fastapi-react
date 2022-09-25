from typing import Any, List
from app import services, models, schemas
from fastapi import APIRouter, Depends, HTTPException, Security, status
from sqlalchemy.orm import Session
from pydantic.types import UUID4
from app.api import deps


router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserDisplay)
def register_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserBase,
) -> Any:
    """
    register user
    """
    user = services.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail='User already exist!',
        )
    user = services.user.register(db, obj_in=user_in)
    return user
