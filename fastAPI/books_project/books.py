from fastapi import FastAPI
# Pydantic is used for data validation and settings management
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int


BOOKS = []


@app.get('/')
async def read_all_books():
    return BOOKS

# using BaseModel means that FastAPI will validate the request body to make sure
# each field is supplied and parse types where necessary (e.g. int to string)
@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book