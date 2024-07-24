# author
from app.api.schemas.author_schema import (
    Author as AuthorSchema,
    AuthorCreate,
    AuthorUpdate,
)

# book
from app.api.schemas.book_schema import (
    Book as BookSchema,
    BookCreate,
    BookUpdate,
)

from app.core.domain.models import Author as AuthorDomain, Book as BookDomain
from app.infrastructure.db.models import Author as AuthorORM, Book as BookORM


# Pydantic to Domain
def map_author_create_to_domain(author: AuthorCreate) -> AuthorDomain:
    return AuthorDomain(
        id=None, name=author.name, bio=author.bio, birth_date=author.birth_date
    )


def map_author_update_to_domain(author: AuthorUpdate, author_id: int) -> AuthorDomain:
    return AuthorDomain(
        id=author_id, name=author.name, bio=author.bio, birth_date=author.birth_date
    )


def map_book_create_to_domain(book: BookCreate) -> BookDomain:
    return BookDomain(
        id=None,
        title=book.title,
        description=book.description,
        publish_date=book.publish_date,
        author_id=book.author_id,
    )


def map_book_update_to_domain(book: BookUpdate, book_id: int) -> BookDomain:
    return BookDomain(
        id=book_id,
        title=book.title,
        description=book.description,
        publish_date=book.publish_date,
        author_id=book.author_id,
    )


# Domain to ORM
def map_author_domain_to_orm(author: AuthorDomain) -> AuthorORM:
    return AuthorORM(
        id=author.id, name=author.name, bio=author.bio, birth_date=author.birth_date
    )


def map_book_domain_to_orm(book: BookDomain) -> BookORM:
    return BookORM(
        id=book.id,
        title=book.title,
        description=book.description,
        publish_date=book.publish_date,
        author_id=book.author_id,
    )


# ORM to Domain
def map_author_orm_to_domain(author: AuthorORM) -> AuthorDomain:
    books = [map_book_orm_to_domain(book) for book in author.books]
    return AuthorDomain(
        id=author.id,
        name=author.name,
        bio=author.bio,
        birth_date=author.birth_date,
        books=books,
    )


def map_book_orm_to_domain(book: BookORM) -> BookDomain:
    return BookDomain(
        id=book.id,
        title=book.title,
        description=book.description,
        publish_date=book.publish_date,
        author_id=book.author_id,
    )


# Domain to Pydantic
def map_author_domain_to_schema(author: AuthorDomain) -> AuthorSchema:
    books = [map_book_domain_to_schema(book) for book in author.books]
    return AuthorSchema(
        id=author.id,
        name=author.name,
        bio=author.bio,
        birth_date=author.birth_date,
        books=books,
    )


def map_book_domain_to_schema(book: BookDomain) -> BookSchema:
    return BookSchema(
        id=book.id,
        title=book.title,
        description=book.description,
        publish_date=book.publish_date,
        author_id=book.author_id,
    )
