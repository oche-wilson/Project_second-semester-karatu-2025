from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email:EmailStr
    is_active: bool = True


users: List[dict] = []