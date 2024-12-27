from fastapi import FastAPI, Path, HTTPException, Query
from typing import Dict

app = FastAPI()

# Для запуска сервера, в терминале используйте команду: uvicorn module_16_3:app --reload

users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_users(
        username: str = Path(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser "),
        age: int = Path(..., ge=18, le=120, description="Enter age", example=24)) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f'User  {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: int = Path(..., ge=1, le=100, description="Enter User ID", example=1),
        username: str = Path(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser "),
        age: int = Path(..., ge=18, le=120, description="Enter age", example=24)) -> str:
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail=f"User  {user_id} not found")

    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User  {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: int = Path(..., ge=1, le=100, description="Enter User ID", example=1)) -> str:
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail=f"User  {user_id} not found")

    users.pop(str(user_id))
    return f"User  {user_id} has been deleted"