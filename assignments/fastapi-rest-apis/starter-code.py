from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    pages: int = Field(..., gt=0)
    available: bool = True

class Book(BookCreate):
    id: int

books: List[Book] = []
next_id = 1

@app.get("/books", response_model=List[Book])
def list_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    global next_id
    new_book = Book(id=next_id, **book.dict())
    books.append(new_book)
    next_id += 1
    return new_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            updated_book = Book(id=book_id, **book.dict())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            books.pop(index)
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")