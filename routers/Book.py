from fastapi import APIRouter, HTTPException
from typing import List
from schemas.Book import Book, Books

Book_route = APIRouter()

@Book_route.get("/", response_model=List[Book])
def get_all_Books():
    return Books

@Book_route.post("/", status_code=201)
def create_Book(Book: Book):
    if any(u["id"] == Book.id for u in Books):
        raise HTTPException(status_code=400, detail="Book ID already exists.")
    Books.append(Book.model_dump())
    return Book

@Book_route.get("/{Book_id}", response_model=Book)
def get_Book(Book_id: int):
    Book = next((u for u in Books if u["id"] == Book_id), None)
    if not Book:
        raise HTTPException(status_code=404, detail="Book cannot be found.")
    return Book

@Book_route.put("/{Book_id}", response_model=Book)
def Book_update (Book_id: int, updated_Book: Book):
    for i, Book in enumerate(Books):
        if Book["id"] == Book_id:
            Books[i] = updated_Book.model_dump()
            return updated_Book
    raise HTTPException(status_code=404, detail="Book cannot be found.")

@Book_route.delete("/{Book_id}")
def Book_delete(Book_id: int):
    global Books
    Books = [u for u in Books if u["id"] != Book_id]
    return {"message": "Book deleted successfully."}

@Book_route.patch("/{Book_id}/Book_Availability")
def Book_Availability(Book_id: int):
    Book = next((u for u in Books if u["id"] == Book_id), None)
    if Book:
        raise HTTPException(status_code=200, detail="Book is Available")
    if not Book:
        raise HTTPException(status_code=404, detail="Book Is not Available.")
    Book["is_active"] = False
    return {"message": "Book is not Available."}