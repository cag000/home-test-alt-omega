from typing import List
from app.infrastructure.repositories.book_repository import BookRepository
from app.common.custom_errors import BadRequestError, InternalServerError, CacheError
from opentelemetry import trace
from app.infrastructure.cache.redis_cache import RedisCache
from app.api.schemas.book_schema import BookCreate, BookUpdate, Book as BookSchema
import json
import logging


tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)


class BookService:
    def __init__(self, book_repository: BookRepository, cache: RedisCache):
        self.book_repository = book_repository
        self.cache = cache

    async def create_book(self, book_data: BookCreate) -> BookSchema:
        with tracer.start_as_current_span("create_book"):
            try:
                book = self.book_repository.create(book_data)
                try:
                    self.cache.delete("books")
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
                return book
            except Exception as e:
                raise InternalServerError("03xx", str(e))

    async def get_books(self, skip: int = 0, limit: int = 10) -> List[BookSchema]:
        with tracer.start_as_current_span("get_books"):
            cache_key = f"books_{skip}_{limit}"
            try:
                cached_books = self.cache.get(cache_key)
                if cached_books:
                    return [
                        BookSchema.parse_obj(book) for book in json.loads(cached_books)
                    ]
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)
            try:
                books = self.book_repository.get_all(skip=skip, limit=limit)
                try:
                    self.cache.set(
                        cache_key, json.dumps([book.dict() for book in books])
                    )
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
                return books
            except Exception as e:
                raise InternalServerError("03xx", str(e))

    async def get_book(self, book_id: int) -> BookSchema:
        with tracer.start_as_current_span("get_book"):
            cache_key = f"book_{book_id}"
            try:
                cached_book = self.cache.get(cache_key)
                if cached_book:
                    return BookSchema.parse_obj(json.loads(cached_book))
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)
            book = self.book_repository.get(book_id)
            if not book:
                raise BadRequestError("01xx", "Book not found")
            try:
                self.cache.set(cache_key, json.dumps(book.dict()))
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)
            return book

    async def update_book(self, book_id: int, book_data: BookUpdate) -> BookSchema:
        with tracer.start_as_current_span("update_book"):
            db_book = self.book_repository.get(book_id)
            if not db_book:
                raise BadRequestError("01xx", "Book not found")
            try:
                updated_book = self.book_repository.update(db_book, book_data)
                try:
                    self.cache.delete(f"book_{book_id}")
                    self.cache.delete("books")
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
                return updated_book
            except Exception as e:
                raise InternalServerError("03xx", str(e))

    async def delete_book(self, book_id: int) -> None:
        with tracer.start_as_current_span("delete_book"):
            try:
                self.book_repository.delete(book_id)
                try:
                    self.cache.delete(f"book_{book_id}")
                    self.cache.delete("books")
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
            except Exception as e:
                raise InternalServerError("03xx", str(e))
