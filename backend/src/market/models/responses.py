import datetime

from pydantic import BaseModel


class ResponseBase(BaseModel):
    order_id: int
    description: str


class ResponseCreate(ResponseBase):
    pass


class Response(ResponseBase):
    id: int
    user_id: int
    created_at: datetime.date
