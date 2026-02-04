# Blogify API 🚀

Blogify is a backend REST API built using FastAPI and PostgreSQL that demonstrates
real-world database modeling, migrations, and one-to-many relationships.

This project focuses on strong backend fundamentals such as ORM design,
schema versioning, clean architecture, and API response validation.

---

## Tech Stack

- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Alembic (database migrations)
- Pydantic v2
- Uvicorn

---

## Features

- Create blog posts
- Add comments to blog posts (One-to-Many relationship)
- Fetch a single blog with nested comments
- Database schema versioning using Alembic
- Clean separation of:
  - Models
  - Schemas
  - Routes
  - Dependencies

---

## Setup Instructions

### 1. Clone the repository

git clone
```bash
https://github.com/Chesta-gaur/blogify-api.git
```
### 2. Create virtual environment

```bash
python -m venv .venv
```
```bash
.venv\scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/blogify_db

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

Server will be available at: http://127.0.0.1:8000

## Key Learning Outcomes

- Implemented relational database models using SQLAlchemy
- Used Alembic for schema versioning and migrations
- Designed clean API contracts with Pydantic response models
- Understood why relationships belong in the database layer
- Built a scalable FastAPI project structure

## Future Enhancements

- List all blogs with pagination
- Update and delete comments
- Authentication and authorization
- Soft deletes and audit fields


