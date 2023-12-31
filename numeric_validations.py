from typing import Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
	item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=1000)],
	size: Annotated[float, Query(gt=0, lt=10.5)],
	q: Annotated[Union[str, None], Query(alias="item-query")] = None,

):
	results = {"item_id": item_id}
	if q:
		results.update({"q": q})
	return results
