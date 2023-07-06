
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional



class UserCreate(BaseModel):
    username: str
    password: str
    salary: int
    promotion_date: Optional[datetime]


class UserOut(BaseModel):
    id: int
    username: str
    salary: int
    promotion_date: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenDate(BaseModel):
    id: Optional[int] = None