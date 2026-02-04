from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.database import Base

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)

    post_id = Column(
        Integer, 
        ForeignKey("blog_posts.id", ondelete="CASCADE"),
        nullable=False
    )

    author_name = Column(String(100), nullable=False)
    comment_text= Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    post = relationship("BlogPost", back_populates="comments")