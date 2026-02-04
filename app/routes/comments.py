from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.comment import Comment
from app.schemas import CommentUpdate

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.patch("/{comment_id}")
def update_comment(
        comment_id: int,
        payload: CommentUpdate,
        db: Session = Depends(get_db)
    ):

    comment = db.get(Comment, comment_id)

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(comment, field, value)

    db.commit()
    db.refresh(comment)
    
    return {"message": "Comment updated successfully"}
