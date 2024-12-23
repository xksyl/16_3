from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_users(username: Annotated[str, Path(min_length=1, max_length=20, description="Имя пользователя")],
    age: Annotated[int, Path(ge=1, le=120, description="Возраст пользователя")]
) -> str:
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, description="ID пользователя")],
    username: Annotated[str, Path(min_length=1, max_length=20, description="Имя пользователя")],
    age: Annotated[int, Path(ge=1, le=120, description="Возраст пользователя")]) -> str:
    user_id_str = str(user_id)
    if user_id_str in users:
        users[user_id_str] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    return f"User {user_id} does not exist"


@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[int, Path(ge=1, description="ID пользователя")]
) -> str:
    user_id_str = str(user_id)
    if user_id_str in users:
        del users[user_id_str]
        return f"User {user_id} has been deleted"
    return f"User {user_id} does not exist"


