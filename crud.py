from  fastapi import   Body,FastAPI

app = FastAPI()



Books = [

    {'title':'title One', 'Author' : 'Author One' , 'Categories' : 'Science'},
    {'title':'title Two', 'Author' : 'Author Two' , 'Categories' : 'Math'},
    {'title':'title Three', 'Author' : 'Author Three' , 'Categories' : 'Physics'},
    {'title':'title Four', 'Author' : 'Author Four' , 'Categories' : 'Chemistry'},
    {'title':'title Five', 'Author' : 'Author Two' , 'Categories' : 'Science'}

]


@app.get("/books")
async def read_all_books():
    return Books


# path parameter
@app.get("/books/{book_title}")
async  def read_all_books(book_title:str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            print(book)
            return book


# Query parameter

@app.get("/books/")
async def read_by_categories(categories:str):
    books_to_return = []
    for book in Books:
        if book.get('Categories').casefold() == categories.casefold():
            books_to_return.append(book)


    return books_to_return


#combination of both path and Query parameter

@app.get("/books/{books_author}/")
async  def ready_by_author_query(books_author:str,categories:str):
    books_to_return = []

    for book in Books:
        if book.get('Author').casefold == books_author.casefold() and book.get('Categories').casefold() == categories.casefold():
            books_to_return.append(book)


    return books_to_return

#Post Method ( for creating data)

@app.post("/books/create_new_book")
async def create_new_book(new_book = Body()):
    Books.append(new_book)


#Put Method( used to update the data)

@app.put("/books/update_the_book")
async def update_the_book(updated_book = Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == updated_book.get('title').casefold():
            Books[i] = updated_book

#Delete Method(used to delete the data)

@app.delete("/books/delete_book_data/{book_title}")
async def delete_book_data(book_title = str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books[i].pop()
            break


#Assignment


@app.get("/books/fetch_all_books/{books_by_author}")
async def fetch_book_by_author(books_by_author:str):
    list_of_result=[]
    for i in range(len(Books)):
        if Books[i].get('Author').casefold() == books_by_author.casefold():
            list_of_result.append(Books[i])

    return list_of_result


