from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None


@app.get("/")
def func():
    return {
        "message": "Hello World!"
    }


@app.post("/data/")
def func(item: Item):
    return {
        "request": item
    }
