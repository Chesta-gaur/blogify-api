from fastapi import FastAPI
from app.routes.blog import router as blog_router
from app.routes.comments import router as comment_router

app = FastAPI(title = "Blogify API")

app.include_router(blog_router)
app.include_router(comment_router)

