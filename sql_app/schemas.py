# from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from fastapi import Body

# class PunishValue(BaseModel):
#     value: int
#
# class PunishCreate(PunishValue):
#     task: str
#
# class Punish(PunishCreate):
#     id: int
#
#     class Config:
#         orm_mode = True

class UserBase(BaseModel):
    username : str
    email : str

class User(UserBase):
    id: int
    is_active :bool
    created_date: Optional[datetime] = Body(None)

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None