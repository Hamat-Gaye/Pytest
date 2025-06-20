from datetime import datetime
from typing import Annotated, List, Optional, Any
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.get("/")
def home_page():
    return "This is the home page"

@app.get("/products")
def get_all_products(products: Annotated[str | None, Query()] = None) -> Any:

    if products is None or len(products)==0:
        return "Product not available"
    return {f"The available production: {products.split(',')}"}

# @app.put("/items/{id}")
# def update_item(id: str, item: Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     fake_db[id] = json_compatible_item_data















