from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connect to a sqlite database & create file "todos.db" storing our database
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# create an engine, these arguments are specific to sqlite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# instance of database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create database model to be inherited
Base = declarative_base()
