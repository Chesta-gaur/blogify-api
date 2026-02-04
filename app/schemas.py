from pydantic import BaseModel
from datetime import datetime
from typing import List

class CommentCreate(BaseModel):
    author_name: str
    comment_text: str

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
