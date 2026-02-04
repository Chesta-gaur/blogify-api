from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.blog_post import BlogPost
from app.models.comment import Comment
from app.schemas import BlogPostCreate, BlogPostUpdate, BlogPostResponse, CommentCreate, BlogPostListResponse

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.get("/")
def home():
    return {
        "message" : "blogify API is running"
    }


@router.get("", response_model=List[BlogPostListResponse])
def list_blogs(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    posts = (
        db.query(BlogPost)
        .order_by((BlogPost.created_at))
        .offset(offset)
        .limit(limit)
        .all()
    )

    return posts


@router.get("/{post_id}", response_model = BlogPostResponse)
def get_blog_post(post_id : int, db : Session = Depends(get_db)):
    post = db.get(BlogPost, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="post not found"
        )
    
    return post


@router.post("",status_code=201, response_model=BlogPostResponse)
def create_blog_post(payload : BlogPostCreate, db: Session = Depends(get_db)):
    post = BlogPost(**payload.model_dump())

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


@router.post("/{post_id}/comments")
def add_comment(post_id : int, payload : CommentCreate, db : Session = Depends(get_db)):
    post = db.get(BlogPost, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="comment not found"
        )
    
    comment = Comment(post_id=post_id, **payload.model_dump())

    db.add(comment)
    db.commit()

    return {
        "message" : "comment added successfully"
    }


@router.patch("/{post_id}", response_model=BlogPostResponse)
def update_blog_post(
        post_id: int,
        payload: BlogPostUpdate,
        db: Session = Depends(get_db)
    ):

    post = db.get(BlogPost, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(post, field, value)

    db.commit()
    db.refresh(post)

    return post


@router.delete("/{post_id}", status_code=204)
def delete_blog_post(post_id : int, db : Session = Depends(get_db)):
    post = db.get(BlogPost, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="post not found"
        )
    
    db.delete(post)
    db.commit()

    return {"message": "Post deleted successfully"}

