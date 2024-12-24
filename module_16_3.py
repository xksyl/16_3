from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_users(username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    new_id = str(max(map(int, users.keys())) + 1) if users else "1"
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int,Path(ge=1, le=100, description="Enter User ID", example=1)],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    user_id_str = str(user_id)
    if user_id_str in users:
        users[user_id_str] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    return f"User {user_id} does not exist"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int,Path(ge=1, le=100, description="Enter User ID", example=1)]) -> str:
    user_id_str = str(user_id)
    if user_id_str in users:
        del users[user_id_str]
        return f"User {user_id} has been deleted"
    return f"User {user_id} does not exist"

