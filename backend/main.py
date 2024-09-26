from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class Item(BaseModel):
    ingredients: str


@app.get("/")
def func():
    return {
        "message": "Hello World!"
    }


@app.post("/test")
def get_recipes(item: Item):
    url = f"https://api.edamam.com/search?q={
        item.ingredients}&app_id={app_id}&app_key={app_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['hits']  # This contains the list of recipes
    else:
        return {
            "message": "There is problem.",
            "code": response.status_code,
            "content": response.content
        }
