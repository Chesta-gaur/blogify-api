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
- List all blogs with pagination (`limit`, `offset`)
- Order blog listings by creation date (latest first)
- Partially update blog posts using PATCH
- Edit comments using PATCH
- Database schema versioning using Alembic
- Clean separation of concerns:
  - Models (database layer)
  - Schemas (request/response contracts)
  - Routes (API layer)
  - Dependencies (DB session management)
- Fully tested using FastAPI’s interactive Swagger UI

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

- Implemented relational database models using SQLAlchemy ORM
- Designed one-to-many relationships and enforced them at the database level
- Used Alembic for database schema versioning and migrations
- Built paginated and ordered list endpoints for scalable data access
- Designed separate schemas for create, update, list, and detail responses
- Implemented safe partial updates using PATCH and `exclude_unset`
- Understood REST design principles for collection vs single-resource endpoints
- Built a scalable and maintainable FastAPI project structure

## Future Enhancements

- Authentication and authorization
- Soft deletes and audit fields


