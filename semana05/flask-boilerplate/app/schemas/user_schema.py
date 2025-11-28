from pydantic import BaseModel, Field
from typing import Annotated

class UserSchema(BaseModel):
    name: str
    last_name: str
    email: str
    password: Annotated[str, Field(min_length=6)]
    role_id: int