from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from databases import Database
from app.infrastructure.db.database import db_engine, primary_database
from app.infrastructure.repositories.author_repository import AuthorRepository
from app.infrastructure.repositories.book_repository import BookRepository
from app.core.services.author_service import AuthorService
from app.core.services.book_service import BookService
from app.infrastructure.cache.redis_cache import RedisCache


def get_db() -> Generator[Session, any, None]:
    db = db_engine.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_database() -> Database:
    return primary_database


def get_cache() -> RedisCache:
    return RedisCache()


def get_author_repository(db: Session = Depends(get_db)) -> AuthorRepository:
    return AuthorRepository(db)


def get_book_repository(db: Session = Depends(get_db)) -> BookRepository:
    return BookRepository(db)


def get_author_service(
    author_repository: AuthorRepository = Depends(get_author_repository),
    cache: RedisCache = Depends(get_cache),
) -> AuthorService:
    return AuthorService(author_repository, cache)


def get_book_service(
    book_repository: BookRepository = Depends(get_book_repository),
    cache: RedisCache = Depends(get_cache),
) -> BookService:
    return BookService(book_repository, cache)
