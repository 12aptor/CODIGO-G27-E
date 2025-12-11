from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

class RegisterSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: Annotated[str, Field(min_length=6)]
    role_id: int

class LoginSchema(BaseModel):
    email: EmailStr
    password: str