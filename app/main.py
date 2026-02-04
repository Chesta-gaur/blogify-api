from fastapi import FastAPI
from app.routes.blog import router as blog_router

app = FastAPI(title = "Blogify API")

app.include_router(blog_router)

