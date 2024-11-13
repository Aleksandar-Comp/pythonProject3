from fastapi import FastAPI, Body, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from typing import List, Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get(path="/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        for user in users:
            if user.id == user_id:
                requested_user = user
                return templates.TemplateResponse("users.html", {"request": request, "user": requested_user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=4, max_length=20, description='Enter username', example="Alex")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="40")]
) -> str:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return f"id: {new_user.id}, username: {new_user.username}, age: {new_user.age}"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, new_username: str = Body(), new_age: int = Body()) -> str:
    for user in users:
        if user.id == user_id:
            user.username = new_username
            user.age = new_age
            return f"id: {user.id}, username: {user.username}, age: {user.age}"
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for index, user in enumerate(users):
        if user.id == user_id:
            user_del = users.pop(index)
            return f"id: {user_del.id}, username: {user_del.username}, age: {user_del.age}"
    raise HTTPException(status_code=404, detail="User was not found")