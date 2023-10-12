from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

import models
from database import engine, SessionLocal
from models import Todos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool



db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/', status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()


# to get the data based on id
@app.get('/todo/{todo_id}', status_code=status.HTTP_200_OK)
async def fetch_based_on_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Data not found')


# post Request to create and save

@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_to_do(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(** todo_request.model_dump())
    db.add(todo_model)
    db.commit()