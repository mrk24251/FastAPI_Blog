# from typing import List, Optional

from pydantic import BaseModel
import datetime
from typing import Optional,List
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

class UserBase2(BaseModel):
    username : str


class User(UserBase):
    id: int
    is_active :bool
    created_date: Optional[datetime.datetime] = Body(None)

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserInDB(BaseModel):
    username: str
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

class CommentBase(BaseModel):
    name: str
    email: str
    body: str

class Comment(CommentBase):
    id: int
    post_id: int
    created_date: Optional[datetime.datetime] = Body(None)
    is_active: bool

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    body: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    url: str
    owner: User
    comment: List[Comment]
    created_date: Optional[datetime.datetime] = Body(None)

    class Config:
        orm_mode = True
