from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import  Optional

app = FastAPI()

class Book:
    id : int
    title : str
    author:str
    description :str
    rating : int

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None
    title:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1 , max_length= 100)
    rating :int = Field(gt=-1 ,lt=6)


    class Config:
        json_schema_extra = {

            'example':{
                'title' : 'A new Book',
                'Author' : ' Dennis Riche',
                'description' : 'This book is awesome to read',
                'rating' : 5



            }
        }



BOOKS = [
    Book(1,'Coding is my part','Liju','A very nice book',5),
    Book(2,'DSA','Raman','Tuff to learn',3),
    Book(3,'A work to be done','Shwetha','A very nice book to learn',5),
    Book(4,'Eating is my habbit ','Liju','A very nice book',5),
    Book(5,'Be happy in good days','Arjun','Great story to learn',5)

]


# API endpoint to retrieve all books
@app.get("/books")
async def read_all_books():
    return BOOKS



@app.post("/create_book")
async  def create_books(new_books: BookRequest):
    newBook = Book(** new_books.dict())
    BOOKS.append(find_id_book(newBook))




def find_id_book(book:Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id+1
    else:
        book.id = 1


    return  book
