from sqlalchemy.orm import Session
from typing import List
from app.infrastructure.db.models import Author, Book
from app.api.schemas.author_schema import AuthorCreate, AuthorUpdate
from app.infrastructure.repositories.base_repository import BaseRepository


class AuthorRepository(BaseRepository[Author, AuthorCreate, AuthorUpdate]):
    def __init__(self, db: Session):
        super().__init__(Author, db)

    def get_books_by_author(self, author_id: int) -> List[Book]:
        return self.db.query(Book).filter(Book.author_id == author_id).all()
