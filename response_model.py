#Note that this section has JsonResponse to directly make the response but only pydantic model
# is in the example

from typing import Any, List, Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
	username: str
	password: str
	email: EmailStr
	full_name: Union[str, None] = None

class UserOut(BaseModel):
	username: str
	email: EmailStr
	full_name: Union[str, None] = None

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
	return user
