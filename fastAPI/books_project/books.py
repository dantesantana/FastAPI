from typing import Optional
# Path allows us to validate path parameters
# Query allows us to validate query parameters
from fastapi import FastAPI, Path, Query, HTTPException
# Pydantic is used for data validation and settings management
from pydantic import BaseModel, Field
# FastAPI is built using starlette, we're using status here to create successful HTTP response codes
from starlette import status
# from uuid import UUID

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    publish_date: int

    def __init__(self, id, title, author, description, rating, publish_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date

# using BaseModel means that FastAPI will validate the request body to make sure
# each field is supplied and parse types where necessary (e.g. int to string)
# creating a request object inheriting from BaseModel means the swagger section for this endpoint will have an example body


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    publish_date: int = Field(gt=1000, lt=3000)

    # Config is a pydantic class, in this way we can specify an example value
    class Config:
        schema_extra = {
            'example': {
                'title': 'new book',
                'author': 'codingwithroby',
                'description': 'book description',
                'rating': 5,
                'publish_date': 2000
            }
        }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby',
         'A very nice book!', 5, 2010),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2010),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome book!', 5, 2011),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2012),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2013),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2014)
]


@app.get('/books', status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail='Book not found')

# using book_rating as a query parameter so it doesn't interfere with read_book
# (where book_id is a path parameter)


@app.get('/books/', status_code=status.HTTP_200_OK)
async def read_books_by_rating(book_rating: int = Query(gt=0, lt=6)):
    book_list = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_list.append(book)
    return book_list


@app.get('/books/publish/', status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(publish_date: int = Query(gt=1000, lt=3000)):
    book_list = []
    for book in BOOKS:
        if book.publish_date == publish_date:
            book_list.append(book)
    return book_list


@app.post('/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    # convert BookRequest object into Book object
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Book not found')


@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Book not found')
