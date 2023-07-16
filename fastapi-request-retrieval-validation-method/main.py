from fastapi import FastAPI, Header, Depends, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item: Item, user_agent: Optional[str] = Header(None)):
    item_dict = item.dict()
    item_dict.update({"user_agent": user_agent})
    return item_dict
