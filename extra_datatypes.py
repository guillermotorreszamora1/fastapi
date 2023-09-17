from datetime import datetime, time, timedelta
from typing import Union
from uuid import UUID


from fastapi import Body, Cookie, Header, FastAPI
from typing_extensions import Annotated

app = FastAPI()

@app.put("Items/{item_id}")
async def read_item(
	item_id: UUID,
	start_datetime: Annotated[Union[datetime, None], Body()] = None,
	end_datetime: Annotated[Union[datetime, None], Body()] = None,
	repeat_at: Annotated[Union[time, None], Body()] = None,
	process_after: Annotated[Union[timedelta, None], Body()] = None,
):
	start_process = start_datetime + process_after
	duration = end_datetime - start_process
	return {
		"item_id": item_id,
		"start_datetime": start_datetime,
		"end_datetime": end_datetime,
		"repeat_at": repeat_at,
		"process_after": process_after,
		"start_process": start_process,
		"duration": duration,
	}

@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
	return {"ads_id": ads_id}

@app.get("/items/")
async def read_items_header(user_agent: Annotated[Union[str, None], Header()] = None):
	return {"User-Agent": user_agent}
