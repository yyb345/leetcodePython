from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Define data model
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

app = FastAPI()

# In-memory database (just a Python list)
items_db: List[Item] = []

# Create an item
@app.post("/items/")
def create_item(item: Item):
    items_db.append(item)
    return {"message": "Item created successfully", "item": item}

# Read all items
@app.get("/items/", response_model=List[Item])
def get_items():
    return items_db

# Read a specific item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db[idx] = updated_item
            return {"message": "Item updated successfully", "item": updated_item}
    return {"error": "Item not found"}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[idx]
            return {"message": "Item deleted successfully"}
    return {"error": "Item not found"}

