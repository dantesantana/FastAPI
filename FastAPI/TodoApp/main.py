from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# get database --> create a session of our database then
# close the database even if the session fails
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
    complete: bool


# READ all todos with dependencies i.e. AFTER the get_db() function is executed successfully
@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


# READ a specific task
@app.get("/todo/{todo_id}")
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    # todo_id of path param needs to match the record of the id in the table
    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .first()
    if todo_model is not None:
        return todo_model
    raise http_exception()


# CREATE a task
@app.post("/")
async def create_todo(todo: Todo, db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    # place an object in the session, will be persisted to the database on the next flush operation
    db.add(todo_model)
    db.commit()

    return successful_response(201)


# UPDATE an existing task
@app.put("/{todo_id}")
async def update_todo(todo_id: int, todo: Todo, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .first()
    # if we couldn't find a match to the requirements above
    if todo_model is None:
        raise http_exception()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(200)


# DELETE a task
@app.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .first()
    if todo_model is None:
        raise http_exception()

    db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .delete()
    db.commit()

    return successful_response(200)


def successful_response(status_code: int):
    return {'status': status_code, 'transaction': 'Successful'}


def http_exception():
    return HTTPException(status_code=404, detail="Todo not found")
