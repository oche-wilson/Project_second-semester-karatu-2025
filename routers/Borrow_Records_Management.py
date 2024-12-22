from fastapi import APIRouter, HTTPException
from schemas.Borrow_Record import borrow_records
from routers.Borrow_Record import find_user_id


Borrow_Manage = APIRouter()


@Borrow_Manage.get("/records/user/{user_id}", status_code=200)
def get_user_records(user_id: int):
    user = find_user_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    user_records = [record for record in borrow_records if record["user_id"] == user_id]
    if not user_records:
        raise HTTPException(status_code=404, detail="No borrowing records found for this user.")

    return {"user_id": user_id, "borrow_records": user_records}


@Borrow_Manage.get("/records")
def get_all_records():
    if not borrow_records:
        raise HTTPException(status_code=404, detail="No borrowing records found.")
    return {"borrow_records": borrow_records}