from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    name: str
    surname: str
    role: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    balance: int
    pending_balance: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
