import random
import shutil
import string
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from app import services, schemas
from app.api import deps
from app.core.security import get_current_user

router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ['absolute', 'relative']


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.PostDisplay)
def create_post(
        *,
        db: Session = Depends(deps.get_db),
        current_user: schemas.UserAuth = Depends(get_current_user),
        request: schemas.PostCreate,
) -> Any:
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=400,
            detail='image url types must be relative or absolute!',
        )
    post = services.post.create(db, obj_in=request)
    return post


@router.get("/all", response_model=List[schemas.PostDisplay])
def get_all_posts(
        *,
        db: Session = Depends(deps.get_db),
) -> Any:
    posts = services.post.get_multi(db)
    return posts


@router.delete("/delete")
def delete_post(
        id: int,
        *,
        db: Session = Depends(deps.get_db),
        current_user: schemas.UserAuth = Depends(get_current_user)
) -> Any:
    services.post.remove(db, id=id, user_id=current_user.id)
    return 'deleted !'


@router.post('/image')
def upload_image(
        image: UploadFile = File(...),
        current_user: schemas.UserAuth = Depends(get_current_user)
):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "a+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}
