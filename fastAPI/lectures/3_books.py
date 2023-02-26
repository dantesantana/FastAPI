from fastapi import FastAPI

app = FastAPI()

# async is "pretty optional for this course, feel free to drop it if you like?"


@app.get('/')
async def first_api():
    return {'message': 'Hello Eric'}


# The API above can be seen when running the following command
# and navigating to the site provided
# uvicorn lectures.3_books:app --reload
# http://127.0.0.1:8000/docs