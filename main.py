from fastapi import FastAPI, Depends

from pyfh.entities import user
from pyfh.config import settings


app = FastAPI()

@app.get("/")
async def test():
    return settings
