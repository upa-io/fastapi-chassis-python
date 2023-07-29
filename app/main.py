from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional 
from typing import Union

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

items = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: Union[int, str], q: Union[str, None] = None) -> dict:
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} eliminado"}

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return Response(status_code=201)

@app.options("/items/")
def get_options():  
    return {"message": "OPTIONS response"}

@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, item: Item):
    return Response(status_code=200)
