from sqlalchemy.orm import Session
from app.infrastructure.db.models import Book
from app.api.schemas.book_schema import BookCreate, BookUpdate
from app.infrastructure.repositories.base_repository import BaseRepository


class BookRepository(BaseRepository[Book, BookCreate, BookUpdate]):
    def __init__(self, db: Session):
        super().__init__(Book, db)
