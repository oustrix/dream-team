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


class Operation(OperationBase):
    id: int
    date: date

    class Config:
        from_attributes = True

