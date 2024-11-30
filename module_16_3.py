from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

users = {'1': 'Имя: Example, возраст: 18'}
@app.get("/")
async def get_main():
    return "Главная страница"

@app.get("/user/admin")
async def get_admin():
    return "Вы вошли, как администратор"

@app.get("/user/{user_id}")
async def get_user_id(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=32)]):
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user/{username}/{age}')
async def get_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get('/users')
async def get_all_users():
    return users

@app.post('/user/{username}/{age}')
async def crate_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    user_id = str(len(users) + 1)
    users.update({user_id: f"Имя: {username}, возраст: {age}"})
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return "The user {user_id} is updated"

@app.delete( '/user/{user_id}')
async def delete_users(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='1')]):
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"

