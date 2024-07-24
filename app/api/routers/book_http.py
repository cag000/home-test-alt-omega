from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.core.services.book_service import BookService
from app.api.schemas.book_schema import BookCreate, BookUpdate, Book as BookSchema
from app.api.schemas.response_schema import (
    SingleObjectResponse,
    ListObjectResponse,
    SuccessResponse,
    ErrorResponse,
)
from app.api.dependencies import get_book_service
from app.common.error_handler import handle_custom_error

router = APIRouter()


@router.post("/", response_model=SingleObjectResponse)
async def create_book(
    book: BookCreate, service: BookService = Depends(get_book_service)
):
    try:
        created_book = await service.create_book(book)
        return {"message": "success", "data": created_book}
    except Exception as e:
        handle_custom_error(e)


@router.get("/", response_model=ListObjectResponse)
async def read_books(
    skip: int = 0, limit: int = 10, service: BookService = Depends(get_book_service)
):
    try:
        books = await service.get_books(skip, limit)
        return {"message": "success", "data": books}
    except Exception as e:
        handle_custom_error(e)


@router.get("/{book_id}", response_model=SingleObjectResponse)
async def read_book(book_id: int, service: BookService = Depends(get_book_service)):
    try:
        book = await service.get_book(book_id)
        return {"message": "success", "data": book}
    except Exception as e:
        handle_custom_error(e)


@router.put("/{book_id}", response_model=SingleObjectResponse)
async def update_book(
    book_id: int, book: BookUpdate, service: BookService = Depends(get_book_service)
):
    try:
        updated_book = await service.update_book(book_id, book)
        return {"message": "success", "data": updated_book}
    except Exception as e:
        handle_custom_error(e)


@router.delete("/{book_id}", response_model=SuccessResponse)
async def delete_book(book_id: int, service: BookService = Depends(get_book_service)):
    try:
        await service.delete_book(book_id)
        return {"message": "success"}
    except Exception as e:
        handle_custom_error(e)
