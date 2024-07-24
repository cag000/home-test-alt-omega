from typing import List, Optional
from datetime import date


class Author:
    def __init__(
        self,
        id: int,
        name: str,
        bio: Optional[str],
        birth_date: date,
        books: Optional[List["Book"]] = None,
    ):
        self.id = id
        self.name = name
        self.bio = bio
        self.birth_date = birth_date
        self.books = books or []


class Book:
    def __init__(
        self,
        id: int,
        title: str,
        description: Optional[str],
        publish_date: date,
        author_id: int,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.publish_date = publish_date
        self.author_id = author_id
