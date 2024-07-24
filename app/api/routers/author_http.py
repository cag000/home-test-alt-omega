from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.core.services.author_service import AuthorService
from app.api.schemas.author_schema import (
    AuthorCreate,
    AuthorUpdate,
    Author as AuthorSchema,
)
from app.api.schemas.book_schema import Book as BookSchema
from app.api.schemas.response_schema import (
    SingleObjectResponse,
    ListObjectResponse,
    SuccessResponse,
    ErrorResponse,
)
from app.api.dependencies import get_author_service
from app.common.error_handler import handle_custom_error

router = APIRouter()


@router.post("/", response_model=SingleObjectResponse)
async def create_author(
    author: AuthorCreate, service: AuthorService = Depends(get_author_service)
):
    try:
        created_author = await service.create_author(author)
        return {"message": "success", "data": created_author}
    except Exception as e:
        handle_custom_error(e)


@router.get("/", response_model=ListObjectResponse)
async def read_authors(
    skip: int = 0, limit: int = 10, service: AuthorService = Depends(get_author_service)
):
    try:
        authors = await service.get_authors(skip, limit)
        return {"message": "success", "data": authors}
    except Exception as e:
        handle_custom_error(e)


@router.get("/{author_id}", response_model=SingleObjectResponse)
async def read_author(
    author_id: int, service: AuthorService = Depends(get_author_service)
):
    try:
        author = await service.get_author(author_id)
        return {"message": "success", "data": author}
    except Exception as e:
        handle_custom_error(e)


@router.put("/{author_id}", response_model=SingleObjectResponse)
async def update_author(
    author_id: int,
    author: AuthorUpdate,
    service: AuthorService = Depends(get_author_service),
):
    try:
        updated_author = await service.update_author(author_id, author)
        return {"message": "success", "data": updated_author}
    except Exception as e:
        handle_custom_error(e)


@router.delete("/{author_id}", response_model=SuccessResponse)
async def delete_author(
    author_id: int, service: AuthorService = Depends(get_author_service)
):
    try:
        await service.delete_author(author_id)
        return {"message": "success"}
    except Exception as e:
        handle_custom_error(e)


@router.get("/{author_id}/books", response_model=ListObjectResponse)
async def get_books_by_author(
    author_id: int, service: AuthorService = Depends(get_author_service)
):
    try:
        books = await service.get_books_by_author(author_id)
        return {"message": "success", "data": books}
    except Exception as e:
        handle_custom_error(e)
