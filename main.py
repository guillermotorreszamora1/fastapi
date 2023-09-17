from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet  = "resnet"
	lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item_int(item_id: int):
	return {"item_id": item_id}

# This is repeated and thus unreachable
@app.get("/items/{item_id}")
async def read_item(item_id):
	return {"item_id": item_id}

@app.get("/users")
async def read_users():
	return ["Rick", "Morty"]

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
	if model_name is ModelName.alexnet:
		return {"model_name": model_name, "message":"Deep Learning FTW!"}
	if model_name.value == "lenet":
		return {"model_name": model_name, "message": "LeCNN all the images"}

	return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
	return {"file_path": file_path}

#Query parameters code
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
	return fake_items_db[skip: skip + limit]


#Request Body
from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
	name: str
	description: Union[str, None] = None
	price: float
	tax: Union[float, None] = None

@app.post("/items/")
async def create_item(item: Item):
	item_dict = item.dict()
	if item.tax:
		price_with_tax = item.price + item.tax
		item_dict.update({"price_with_tax": price_with_tax})
	return item_dict
	return item
