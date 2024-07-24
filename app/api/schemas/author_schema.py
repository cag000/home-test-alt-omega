from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from app.core.domain.models import Book


class AuthorBase(BaseModel):
    name: str = Field(..., example="J.K. Rowling")
    bio: Optional[str] = Field(None, example="Author of the Harry Potter series")
    birth_date: date = Field(..., example="1965-07-31")


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class AuthorWithBooks(Author):
    books: Optional[List[Book]] = []
