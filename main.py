from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def f_index():
    return {"FIO": "Каплунов Александр Артемович"}


@app.get('/tools')
async def f_index():
    return {"message": "tools", "key": "junior"}


@app.get('/users')
async def f_index():
    return {"message": "users", "key": "+79293460544"}
