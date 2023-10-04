from enum import Enum
from typing import Optional

from pydantic import BaseModel
from datetime import date


class OrderStatus(str, Enum):
    OPEN = 'open'
    IN_PROCESS = 'in_process'
    DECLINED = 'declined'
    CLOSED = 'closed'


class OrderBase(BaseModel):
    title: str
    description: str
    reward: int


class Order(OrderBase):
    id: int
    owner_id: int
    status: OrderStatus
    worker_id: Optional[int]
    create_at: Optional[date]
    assigned_at: Optional[date]
    closed_at: Optional[date]

    class Config:
        from_attributes = True


class OrderCreate(OrderBase):
    pass
