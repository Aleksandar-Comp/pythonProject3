from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def registration(username: Annotated[
    str, Path(min_length=3, max_length=16, description="Enter username", example="PashaTehnik")],
                       age: int = Path(ge=18, le=60, description="Enter age", example="48")) -> str:
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return f"The user {new_user} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int,
                      username: Annotated[str, Path(min_length=3, max_length=16, description="Enter username", example="PashaTehnik")],
                      age: int = Path(ge=18, le=60, description="Enter age", example="48")) -> str:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return f"User {user_id} has been updated"
    except:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def deleted_user(user_id: int) -> str:
    try:
        users.pop(user_id - 1)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")