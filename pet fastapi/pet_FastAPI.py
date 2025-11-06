from fastapi import FastAPI, HTTPException, BackgroundTasks, File, UploadFile          #грустно но по сути бекграундтаск со старлета
from authx import AuthX, AuthXConfig
from pydantic import BaseModel
from fastapi.responses import StreamingResponse, FileResponse
import time
import uvicorn
import asyncio
import pytest

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SEKRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config = config)


class userloginschema(BaseModel):                  #схема для логина
    username: str
    password: str

@app.post("/login")                       #логин простая ручка
def login(credentials: userloginschema):
    if credentials.username == "admin" and credentials.password == "password":
        token = security.create_access_token(uid="1211")
        return {"token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
@app.get("/protected")                  #защищенная ручка
def protected():
    return {"message": "This is a protected route"}


def sync_task():                        #синхронная задача
    time.sleep(10)
    print("Отправлен ответ")

async def async_task():                  #асинхронная задача
    await asyncio.sleep(10)
    print("сделан запрос")
    
@app.get("/")
async def root():
    return {"message": "Welcome to Pet FastAPI!"}


@app.post("/")                         #асинхронная доп ручка
async def async_endpoint(bg_tasks: BackgroundTasks):
    ...
    #asyncio.create_task(async_task())     #фоновое асинхронное задание
    bg_tasks.add_task(async_task)         # возмонжо будет не актуально будет если синхронки обойдут
    return {"ok": True}

@app.post("/multiupload")
async def upload_file(upload_files: list[UploadFile] = File(...)):
    for upload_file in upload_files:
        file = upload_file.file                 #выгрузка файлa
        filename = upload_file.filename
        with open(filename, "wb") as f:
            f.write(file.read())
            
            
def iter_files(filename: str):
    with open(filename, "rb") as f:
        while chunk := f.read(1024 * 1024):
            yield chunk
            
            
            
@app.get("/download")
async def download_file(filename: str):           #получение файла
    return StreamingResponse(iter_files(filename), media_type="application/octet-stream")