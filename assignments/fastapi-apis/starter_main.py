from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

_db: List[Item] = []

@app.get("/items", response_model=List[Item])
def list_items():
    return _db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in _db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", status_code=201, response_model=Item)
def create_item(item: Item):
    if any(i.id == item.id for i in _db):
        raise HTTPException(status_code=400, detail="ID already exists")
    _db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for idx, item in enumerate(_db):
        if item.id == item_id:
            _db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, item in enumerate(_db):
        if item.id == item_id:
            _db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")
