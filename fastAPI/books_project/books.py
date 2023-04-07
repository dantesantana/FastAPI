from typing import Optional

from fastapi import FastAPI
# Pydantic is used for data validation and settings management
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# using BaseModel means that FastAPI will validate the request body to make sure
# each field is supplied and parse types where necessary (e.g. int to string)
# creating a request object inheriting from BaseModel means the swagger section for this endpoint will have an example body


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    # Config is a pydantic class, in this way we can specify an example value
    class Config:
        schema_extra = {
            'example': {
                'title': 'new book',
                'author': 'codingwithroby',
                'description': 'book description',
                'rating': 5
            }
        }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1)
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get('/books/{book_id}')
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

# using book_rating as a query parameter so it doesn't interfere with read_book
# (where book_id is a path parameter)


@app.get('/books/')
async def read_book_by_rating(book_rating: int):
    book_list = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_list.append(book)
    return book_list


@app.post('/create-book')
async def create_book(book_request: BookRequest):
    # convert BookRequest object into Book object
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))
    return new_book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put('/books/update_book')
async def update_book(book: BookRequest)
