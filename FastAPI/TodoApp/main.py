from fastapi import FastAPI, Depends
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# read all entries in a table with dependencies i.e. AFTER the get_db() function is executed
@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()
