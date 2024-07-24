from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class BookBase(BaseModel):
    title: str = Field(..., example="Harry Potter and the Philosopher's Stone")
    description: Optional[str] = Field(None, example="A young wizard's journey begins")
    publish_date: date = Field(..., example="1997-06-26")
    author_id: int = Field(..., example=1)


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BaseModel):
    id: int

    class Config:
        from_attributes = True
