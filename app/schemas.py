from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class CommentCreate(BaseModel):
    author_name: str
    comment_text: str

class CommentUpdate(BaseModel):
    comment_text : Optional[str] = None

class CommentResponse(BaseModel):
    id: int
    author_name: str
    comment_text: str
    created_at: datetime

    model_config = {
        "from_attributes" : True
    }

class BlogPostCreate(BaseModel):
    title : str
    content : str

class BlogPostUpdate(BaseModel):
    title : Optional[str] = None
    content : Optional[str] = None

class BlogPostResponse(BaseModel):
    id : int
    title: str
    content: str
    created_at : datetime
    updated_at : datetime
    comments : List[CommentResponse] = []

    model_config = {
        "from_attributes" : True
    }

class BlogPostListResponse(BaseModel):
    id : int
    title: str
    content: str
    created_at : datetime
    updated_at : datetime
    comments : List[CommentResponse] = []


    model_config = {
        "from_attributes" : True
    }