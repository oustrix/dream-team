from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBase(BaseModel):
    kind: OperationKind
    amount: Decimal
    description: Optional[str]
    date: date


class Operation(OperationBase):
    id: int

    class Config:
        from_attributes = True


class OperationCreate(OperationBase):
    pass
