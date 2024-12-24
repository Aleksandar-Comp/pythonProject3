from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get('/users')
def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}') # запрос регистрация пользователя
def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}') # запрос на изменение данных пользователя
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')

@app.delete('/user/{user_id}') # запрос на удаление конкретного пользователя
def delite_user(user_id: int) -> str:
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')
