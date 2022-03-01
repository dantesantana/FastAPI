from typing import Optional
from fastapi import FastAPI, HTTPException
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

    # set default values using an inner-class
    class Config:
        schema_extra = {
            "example": {
                "id": "01a76169-858e-471f-9b97-575a86b4b588",
                "title": "Computer Science Pro",
                "author": "Codingwithroby",
                "description": "A very nice description of a book",
                "rating": 75
            }
        }


BOOKS = []


# READ all books or a set number of "books_to_return"
@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
    return BOOKS


# READ a specified book
@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_item_cannot_be_found_exception()


# CREATE a book
@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


# UPDATE a book
@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise raise_item_cannot_be_found_exception()


# DELETE a book
@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted'
    # creating an exception (raise runs the current line then stops execution)
    raise raise_item_cannot_be_found_exception()


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


def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404,
                         detail="Book not found",
                         headers={"X-Header_Error":
                                  "Nothing to be seen at the UUID"})
