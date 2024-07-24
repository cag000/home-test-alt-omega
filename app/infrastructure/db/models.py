from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    bio = Column(Text, nullable=True)
    birth_date = Column(Date, nullable=False)

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name}, bio={self.bio}, birth_date={self.birth_date})>"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    publish_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, description={self.description}, publish_date={self.publish_date}, author_id={self.author_id})>"
