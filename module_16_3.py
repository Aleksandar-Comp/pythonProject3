from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def registration(username: Annotated[str, Path(min_length=3, max_length=16, description="Enter username", example="PashaTehnik")],
                       age: int = Path(ge=18, le=60, description="Enter age", example="48")) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: Annotated[str, Path(min_length=3, max_length=16, description="Enter username", example="PashaTehnik")],
                      age: int = Path(ge=18, le=60, description="Enter age", example="48")) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def deleted_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"