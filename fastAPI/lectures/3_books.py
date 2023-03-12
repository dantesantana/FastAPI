from typing import Optional
from fastapi import FastAPI
from enum import Enum
# The API above can be seen when running the following command
# and navigating to the site provided
# uvicorn lectures.3_books:app --reload
# http://localhost:8000/docs

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


class DirectionName(str, Enum):
    north, south, east, west = 'North', 'South', 'East', 'West'


# async is "optional for this course, feel free to drop it if you like"
# skip_book has been made an optional "query parameter"
@app.get('/')
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


# Note that function definitions with path parameters must be defined
# after other functions using the same path
# For example; /foo/{bar} needs to be defined before /foo/baz
# so that 'baz' isn't interpreted as a value for the parameter 'bar'


@app.get('/{book_name}')
async def read_book(book_name: str):
    return BOOKS[book_name]


# Using query parameters to create books
@app.post('/')
async def create_book(book_title, book_author):
    current_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x

    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title,
                                            'author': book_author}
    return BOOKS[f'book_{current_book_id + 1}']

# in this request, we have a path parameter (book_name)
# and two query parameters (book_name & book_author)


@app.put('/{book_name}')
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = book_information
    return book_information

# # enumerations in a path parameter, this provides a list of options in the swagger docs
# @app.get('/directions/{direction_name}')
# async def get_direction(direction_name: DirectionName):
#     if direction_name == DirectionName.north:
#         return {'Direction': direction_name, 'sub': 'Up'}
#     if direction_name == DirectionName.south:
#         return {'Direction': direction_name, 'sub': 'Down'}
#     if direction_name == DirectionName.east:
#         return {'Direction': direction_name, 'sub': 'Right'}
#     return {'Direction': direction_name, 'sub': 'Left'}
