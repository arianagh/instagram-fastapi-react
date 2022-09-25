from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import services, schemas
from app.api import deps
from app.api.deps import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/comment", tags=["comment"])

image_url_types = ['absolute', 'relative']


@router.get("/all/{post_id}")
def get_all_comments(
        *,
        post_id: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    comments = services.comment.get_all(db, post_id=post_id)
    return comments


@router.post('/create')
def create(
        request: schemas.CommentBase,
        db: Session = Depends(get_db),
        current_user: schemas.UserAuth = Depends(get_current_user)
):
    comment = services.comment.create(db, obj_in=request)
    return comment
