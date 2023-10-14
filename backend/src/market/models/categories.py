from pydantic import BaseModel


class CategoryBase(BaseModel):
    id: int
    name: str


class Category(CategoryBase):
    pass
