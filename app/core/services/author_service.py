from typing import List
from app.infrastructure.repositories.author_repository import AuthorRepository
from app.common.custom_errors import BadRequestError, InternalServerError, CacheError
from opentelemetry import trace
from app.infrastructure.cache.redis_cache import RedisCache
from app.api.schemas.author_schema import (
    AuthorCreate,
    AuthorUpdate,
    Author as AuthorSchema,
    Book as BookSchemaa,
)
from app.core.mappers import *
import json
import logging

tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)


class AuthorService:
    def __init__(self, author_repository: AuthorRepository, cache: RedisCache):
        self.author_repository = author_repository
        self.cache = cache

    async def create_author(self, author_data: AuthorCreate) -> AuthorSchema:
        with tracer.start_as_current_span("create_author"):
            try:
                domain_author = map_author_create_to_domain(author_data)
                author = map_author_orm_to_domain(
                    self.author_repository.create(
                        map_author_domain_to_orm(
                            domain_author,
                        )
                    )
                )
                try:
                    self.cache.delete("authors")
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
                return map_author_domain_to_schema(author)
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)
            except Exception as e:
                raise InternalServerError("03xx", str(e))

    async def get_authors(self, skip: int = 0, limit: int = 10) -> List[AuthorSchema]:
        with tracer.start_as_current_span("get_authors"):
            cache_key = f"authors_{skip}_{limit}"
            try:
                cached_authors = self.cache.get(cache_key)
                if cached_authors:
                    return [
                        AuthorSchema.parse_obj(author)
                        for author in json.loads(cached_authors)
                    ]
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)
            try:
                authors = map_author_orm_to_domain(
                    self.author_repository.get_all(skip=skip, limit=limit)
                )
                try:
                    self.cache.set(
                        cache_key,
                        json.dumps(
                            [
                                map_author_domain_to_schema(author).dict()
                                for author in authors
                            ]
                        ),
                    )
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
                return [map_author_domain_to_schema(author) for author in authors]
            except Exception as e:
                raise InternalServerError("03xx", str(e))

    async def get_author(self, author_id: int) -> AuthorSchema:
        with tracer.start_as_current_span("get_author"):
            cache_key = f"author_{author_id}"
            try:
                cached_author = self.cache.get(cache_key)
                if cached_author:
                    return AuthorSchema.parse_obj(json.loads(cached_author))
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)

            author = map_author_orm_to_domain(self.author_repository.get(author_id))
            if not author:
                raise BadRequestError("01xx", "Author not found")
            try:
                self.cache.set(
                    cache_key,
                    json.dumps(map_author_domain_to_schema(author).model_dump()),
                )
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)
            return map_author_domain_to_schema(author)

    async def update_author(
        self, author_id: int, author_data: AuthorUpdate
    ) -> AuthorSchema:
        with tracer.start_as_current_span("update_author"):
            db_author = self.author_repository.get(author_id)
            if not db_author:
                raise BadRequestError("01xx", "Author not found")
            try:
                domain_author = map_author_update_to_domain(author_data, author_id)
                updated_author = map_author_orm_to_domain(
                    self.author_repository.update(
                        db_author, map_author_domain_to_orm(domain_author)
                    )
                )
                try:
                    self.cache.delete(f"author_{author_id}")
                    self.cache.delete("authors")
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
                return map_author_domain_to_schema(updated_author)
            except Exception as e:
                raise InternalServerError("03xx", str(e))

    async def delete_author(self, author_id: int) -> None:
        with tracer.start_as_current_span("delete_author"):
            try:
                self.author_repository.delete(author_id)
                try:
                    self.cache.delete(f"author_{author_id}")
                    self.cache.delete("authors")
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
            except Exception as e:
                raise InternalServerError("03xx", str(e))

    async def get_books_by_author(self, author_id: int) -> List[BookSchemaa]:
        with tracer.start_as_current_span("get_books_by_author"):
            cache_key = f"author_{author_id}_books"
            try:
                cached_books = self.cache.get(cache_key)
                if cached_books:
                    return [
                        BookSchemaa.parse_obj(book) for book in json.loads(cached_books)
                    ]
            except CacheError as cache_exception:
                logger.warning(cache_exception.message)
            try:
                books = map_author_domain_to_schema(
                    map_author_orm_to_domain(
                        self.author_repository.get_books_by_author(author_id)
                    )
                )
                try:
                    self.cache.set(
                        cache_key, json.dumps([book.dict() for book in books])
                    )
                except CacheError as cache_exception:
                    logger.warning(cache_exception.message)
                return books
            except Exception as e:
                raise InternalServerError("03xx", str(e))
