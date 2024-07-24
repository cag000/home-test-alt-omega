from typing import List, Optional
from abc import ABC, abstractmethod
from app.core.domain.models import Author, Book


class AuthorServiceInterface(ABC):
    @abstractmethod
    async def get_author(self, author_id: int) -> Optional[Author]:
        pass

    @abstractmethod
    async def get_authors(self, skip: int, limit: int) -> List[Author]:
        pass

    @abstractmethod
    async def create_author(self, author: Author) -> Author:
        pass

    @abstractmethod
    async def update_author(self, author_id: int, author: Author) -> Author:
        pass

    @abstractmethod
    async def delete_author(self, author_id: int) -> None:
        pass

    @abstractmethod
    async def get_books_by_author(self, author_id: int) -> List[Book]:
        pass


class BookServiceInterface(ABC):
    @abstractmethod
    async def get_book(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    async def get_books(self, skip: int, limit: int) -> List[Book]:
        pass

    @abstractmethod
    async def create_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    async def update_book(self, book_id: int, book: Book) -> Book:
        pass

    @abstractmethod
    async def delete_book(self, book_id: int) -> None:
        pass
