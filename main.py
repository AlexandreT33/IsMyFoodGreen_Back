from typing import Union

from fastapi import FastAPI
from openfood import OpenFoodApi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/products")
def read_product():
    api = OpenFoodApi().api
    product = api.product.get("3017620422003")
    return {
        "abbreviated_product_name_fr": product['product']['abbreviated_product_name_fr'],
        "brands": product['product']['brands'],
        "images": product['product']['selected_images']['front'],
        "eco": product['product']['ecoscore_data']
    }