from fastapi import APIRouter, HTTPException
from typing import List
from schemas.user import User, users

user_route = APIRouter()

@user_route.get("/", response_model=List[User])
def get_all_users():
    return users

@user_route.post("/")
def user_create(user: User):
    if any(u["id"] == user.id for u in users):
        raise HTTPException(status_code=400, detail="User ID already exists.")
    users.append(user.dict())
    return user


@user_route.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User cannot be found.")
    return user

@user_route.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i] = updated_user.model_dump()
            return updated_user
    raise HTTPException(status_code=404, detail="User cannot be found.")

@user_route.delete("/{user_id}")
def user_delete(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted successfully."}

@user_route.patch("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User cannot found.")
    user["is_active"] = False
    return {"message": "User deactivated Successfully."}
