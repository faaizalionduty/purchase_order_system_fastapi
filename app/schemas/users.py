from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:str

class UserOut(BaseModel):
    username:str
    email:EmailStr
    role:str
    is_active:bool

    class Config:
        from_attributes = True


class LoginCreate(BaseModel):
    email:EmailStr
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

