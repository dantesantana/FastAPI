from typing import Optional

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'}
}


# class DirectionName(str, Enum):
#     north = "North"
#     south = "South"
#     east = "East"
#     west = "West"

# define an optional query parameter called "skip_book"
@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


# using path parameters
@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]

# # using enumerations within a path parameter
# @app.get("/directions/{direction_name}")
# async def get_direction(direction_name: DirectionName):
#     if direction_name == DirectionName.north:
#         return {"Direction": direction_name, "sub": "Up"}
#     if direction_name == DirectionName.south:
#         return {"Direction": direction_name, "sub": "Down"}
#     if direction_name == DirectionName.west:
#         return {"Direction": direction_name, "sub": "Left"}
#     return {"Direction": direction_name, "sub": "Right"}


# @app.get("/books/mybook")
# async def read_favorite_book():
#     return {"book_title": "My favorite book"}


# # to use path parameters, we need to map sure to declare them underneath functions using the same path
# # i.e. read_book must be declared after read_favorite_book so "mybook" isn't interpreted as a value for "book_title"
# @app.get("/books/{book_title}")
# async def read_book(book_id: int):
#     return {"book_title": book_id}
