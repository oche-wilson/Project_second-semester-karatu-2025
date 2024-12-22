from pydantic import BaseModel
from datetime import date

books = [
    {"id": 1, "title": "Book_Title_1", "author": "Author_1", "is_available": True},
]

users = [
    {"id": 1, "name": "Username1", "email": "Username1@example.com", "is_active": True},
]

borrow_records = []

class Borrow_request(BaseModel):
    user_id: int
    book_id: int

class Return_request(BaseModel):
    user_id: int
    book_id: int

    
