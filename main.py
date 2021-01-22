from fastapi import FastAPI, Depends
from pyfh.entities import user

app = FastAPI()


@app.get("/")
async def test():
    return "Welcome to pyfh!"
