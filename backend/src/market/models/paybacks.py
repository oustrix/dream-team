from pydantic import BaseModel

class BasePayback(BaseModel):
    name: str
    count: int
    units: str
    price: int

class Payback(BasePayback):
    id: int