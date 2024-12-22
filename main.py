from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
from routers.user import user_route
from routers.Book import Book_route
from routers.Borrow_Record import Borrow_route
from routers.Borrow_Records_Management import Borrow_Manage
from fastapi.responses import FileResponse


app = FastAPI( )


@app.get("/")
def home():
    return {"Welcome to my E-Library API System"}


app.include_router(user_route, prefix="/user", tags=["Users"])
app.include_router(Book_route, prefix="/Book", tags=["Books"])
app.include_router(Borrow_route, prefix="/Borrow_Record", tags=["Borrow_Operations"])
app.include_router(Borrow_Manage, prefix="/Borrow_Records_Management", tags=["Borrow_Records_Management"])