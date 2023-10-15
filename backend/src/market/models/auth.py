from enum import Enum

from pydantic import BaseModel


class UserRole(str, Enum):
    WORKER = 'worker'
    CUSTOMER = 'customer'


class BaseUser(BaseModel):
    email: str
    name: str
    surname: str
    role: UserRole


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    balance: int
    pending_money: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
