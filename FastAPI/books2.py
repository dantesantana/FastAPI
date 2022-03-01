from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


# setup a Book class inheriting from BaseModel for validation
class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    # description is optional, but must be between 1 & 100 characters long
    description: Optional[str] = Field(title="Description of the book", max_length=100, min_length=1)
    # integer must be between 0 & 100 inclusive
    rating: int = Field(gt=-1, lt=101)


BOOKS = []


# READ all books
@app.get("/")
async def read_all_books():
    if len(BOOKS) < 1:
        create_books_no_api()
    return BOOKS


# CREATE a book
@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

# Initialize books, mainly for development purposes
def create_books_no_api():
    book_1 = Book(id="07a76169-858e-471f-9b97-575a86b4b588",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60)
    book_2 = Book(id="17a76169-858e-471f-9b97-575a86b4b588",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70)
    book_3 = Book(id="27a76169-858e-471f-9b97-575a86b4b588",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80)
    book_4 = Book(id="37a76169-858e-471f-9b97-575a86b4b588",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=90)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
