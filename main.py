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

@app.get("/products/{token}")
def read_product(token : str, q: Union[str, None] = None):
    api = OpenFoodApi().api
    product = api.product.get(token)
    return {
        "abbreviated_product_name_fr": product['product'].get('abbreviated_product_name_fr', "Inconnu"),
        "generic_name": product['product'].get('product_name', "Inconnu"),
        "brands": product['product'].get('brands', "Inconnu"),
        "images": product['product']['selected_images'].get('front'),
        "eco": product['product'].get('ecoscore_data')
    }